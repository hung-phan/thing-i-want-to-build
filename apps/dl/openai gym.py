import gym
import numpy as np
import tensorflow as tf


def train_nn_without_policy_gradient():
    num_inputs = 4
    num_hidden = 4
    num_outputs = 1  # left or right

    initializer = tf.contrib.layers.variance_scaling_initializer()

    # noinspection PyPep8Naming
    X = tf.placeholder(tf.float32, shape=[None, num_inputs])

    hidden_layer_one = tf.layers.dense(X, num_hidden, activation=tf.nn.relu, kernel_initializer=initializer)
    hidden_layer_two = tf.layers.dense(hidden_layer_one, num_hidden, activation=tf.nn.relu,
                                       kernel_initializer=initializer)
    output_layer = tf.layers.dense(hidden_layer_two, num_outputs, activation=tf.nn.sigmoid,
                                   kernel_initializer=initializer)

    probabilities = tf.concat(axis=1, values=[output_layer, 1 - output_layer])
    action = tf.multinomial(probabilities, num_samples=1)

    init = tf.global_variables_initializer()

    epi = 50
    step_limit = 500


    env = gym.make('CartPole-v0')

    with tf.Session() as sess:
        avg_steps = []
        sess.run(init)

        for _ in range(epi):
            obs = env.reset()

            for step in range(step_limit):
                action_val = action.eval(feed_dict={X: obs.reshape(1, num_inputs)})
                obs, reward, done, info = env.step(action_val[0][0])

                if done:
                    avg_steps.append(step)
                    print(f"Done after {step} steps")
                    break

        print(f"After {epi}, average steps per game was {np.mean(avg_steps)}")


def helper_discount_rewards(rewards, discount_rate):
    """
    Takes in rewards and applies discount rate
    """
    discounted_rewards = np.zeros(len(rewards))
    cumulative_rewards = 0
    for step in reversed(range(len(rewards))):
        cumulative_rewards = rewards[step] + cumulative_rewards * discount_rate
        discounted_rewards[step] = cumulative_rewards
    return discounted_rewards


def discount_and_normalize_rewards(all_rewards, discount_rate):
    """
    Takes in all rewards, applies helper_discount function and then normalizes
    using mean and std.
    """
    all_discounted_rewards = []
    for rewards in all_rewards:
        all_discounted_rewards.append(helper_discount_rewards(rewards, discount_rate))

    flat_rewards = np.concatenate(all_discounted_rewards)
    reward_mean = flat_rewards.mean()
    reward_std = flat_rewards.std()
    return [(discounted_rewards - reward_mean) / reward_std for discounted_rewards in all_discounted_rewards]


def train_nn_with_policy_gradient():
    num_inputs = 4
    num_hidden = 4
    num_outputs = 1  # left or right
    learning_rate = 0.01

    initializer = tf.contrib.layers.variance_scaling_initializer()

    # noinspection PyPep8Naming
    X = tf.placeholder(tf.float32, shape=[None, num_inputs])

    hidden_layer = tf.layers.dense(X, num_hidden, activation=tf.nn.elu, kernel_initializer=initializer)
    logits = tf.layers.dense(hidden_layer, num_outputs)
    outputs = tf.nn.sigmoid(logits)

    probabilities = tf.concat(axis=1, values=[outputs, 1 - outputs])
    action = tf.multinomial(probabilities, num_samples=1)

    y = 1.0 - tf.to_float(action)

    cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=logits)

    optimizer = tf.train.AdamOptimizer(learning_rate)

    gradients_and_variables = optimizer.compute_gradients(cross_entropy)

    gradients = []
    gradient_placeholders = []
    grads_and_vars_feed = []

    for gradient, variable in gradients_and_variables:
        gradient_placeholder = tf.placeholder(tf.float32, shape=gradient.get_shape())

        gradients.append(gradient)
        gradient_placeholders.append(gradient_placeholder)
        grads_and_vars_feed.append((gradient_placeholder, variable))

    training_op = optimizer.apply_gradients(grads_and_vars_feed)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()
    env = gym.make('CartPole-v0')

    num_game_rounds = 10
    max_game_steps = 1000
    num_iterations = 650
    discount_rate = 0.9

    with tf.Session() as sess:
        sess.run(init)

        for iteration in range(num_iterations):
            print(f"on iteration: {iteration}")

            all_rewards = []
            all_gradients = []

            for game in range(num_game_rounds):
                current_rewards = []
                current_gradients = []
                observations = env.reset()

                for step in range(max_game_steps):
                    action_val, gradients_val = sess.run([action, gradients], feed_dict={
                        X: observations.reshape(1, num_inputs)
                    })

                    observations, reward, done, info = env.step(action_val[0][0])

                    current_rewards.append(reward)
                    current_gradients.append(gradients_val)

                    if done:
                        break

                all_rewards.append(current_rewards)
                all_gradients.append(current_gradients)

            all_rewards = discount_and_normalize_rewards(all_rewards, discount_rate)
            feed_dict = {}

            for var_index, gradient_placeholder in enumerate(gradient_placeholders):
                mean_gradients = np.mean([reward * all_gradients[game_index][step][var_index]
                                          for game_index, rewards in enumerate(all_rewards)
                                          for step, reward in enumerate(rewards)], axis=0)
                feed_dict[gradient_placeholder] = mean_gradients

            sess.run(training_op, feed_dict=feed_dict)

        tf.train.export_meta_graph(filename="./models/openai-policy-model.meta")
        saver.save(sess, "./models/openai-policy-model")

    observations = env.reset()

    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph("./models/openai-policy-model.meta")
        new_saver.restore(sess, "./models/openai-policy-model")

        for _ in range(500):
            env.render()

            action_val, gradients_val = sess.run([action, gradients], feed_dict={
                X: observations.reshape(1, num_inputs)
            })

            observations, reward, done, info = env.step(action_val[0][0])


if __name__ == '__main__':
    # train_nn_without_policy_gradient()
    train_nn_with_policy_gradient()
