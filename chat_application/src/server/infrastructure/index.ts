import { shutdown as shutdownRedis } from "./redis";
import { shutdown as shutdownPubSub } from "./pubsub";

export const shutdown = () => {
  shutdownRedis();
  shutdownPubSub();
};

export { default as server } from "./server";
