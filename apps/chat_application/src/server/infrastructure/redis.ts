import * as redis from "redis";
import { RedisClient } from "redis";

export const createRedisConnection = (options: Object = {}): RedisClient => {
  if (process.env.NODE_ENV === "production") {
    if (!("host" in options)) {
      options = {
        ...options,
        host: "redis"
      };
    }
  }

  return redis.createClient(options);
};
export const conn = createRedisConnection();
export const shutdown = () => {
  conn.quit();
};
