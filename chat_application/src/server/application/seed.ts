import { range } from "lodash";
import { shutdown } from "../infrastructure";
import { create } from "../domain/repositories/user";
import factory from "../../shared/domain/models/factories";

(async () => {
  await Promise.all(
    range(100).map(async () => create(await factory.build("User")))
  );
  shutdown();
})();
