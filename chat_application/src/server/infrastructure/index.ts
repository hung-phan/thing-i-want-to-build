import ws from "./websocket";
import { shutdown as shutdownRedis } from "./redis";
import { shutdown as shutdownPubSub } from "./pubsub";

export const shutdown = () => {
  ws.close();
  shutdownRedis();
  shutdownPubSub();
};

export { default as server } from "./server";
