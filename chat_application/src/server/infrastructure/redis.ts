import * as redis from "redis";

export const conn = redis.createClient();

export const pub = redis.createClient();

export const sub = redis.createClient();

export const quit = () => {
  conn.quit();
  pub.quit();
  sub.quit();
};

for (const event of ["exit", "SIGINT", "uncaughtException"]) {
  process.on(event, quit);
}
