import { range } from "lodash";
import { quit } from "../infrastructure/redis";
import factory from "../../shared/domain/models/factories";
import { create } from "../domain/repositories/user";

(async () => {
  await Promise.all(
    range(100).map(async () => create(await factory.build("User")))
  );
  quit();
})();
