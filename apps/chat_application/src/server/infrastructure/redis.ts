import * as redis from "redis";

export const conn = redis.createClient();
export const shutdown = () => {
  conn.quit();
};
