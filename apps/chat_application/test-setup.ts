import { shutdown as shutDownRedis } from "./src/server/infrastructure/redis";
import { shutdown as shutDownPubSub } from "./src/server/infrastructure/pubsub";

afterAll(async () => {
  shutDownRedis();
  shutDownPubSub();
});
