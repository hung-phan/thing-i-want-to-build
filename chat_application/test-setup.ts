import { quit } from "./src/server/infrastructure/redis";

afterAll(async () => {
  quit();
});
