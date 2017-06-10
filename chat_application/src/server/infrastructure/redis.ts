import * as redis from "redis";

export const conn = redis.createClient();

for (const event of ["exit", "SIGINT", "uncaughtException"]) {
  process.on(event, () => {
    conn.quit();
  });
}
