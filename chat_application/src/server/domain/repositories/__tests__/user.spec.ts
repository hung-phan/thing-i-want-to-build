import { create, get, remove } from "../user";
import factory from "../../../../shared/domain/models/factories";

let user;

beforeAll(async () => {
  user = await factory.build("User");
});

test("create", async () => {
  expect(await create(user)).toBe("OK");
});

test("get", async () => {
  expect(await get(user.id)).toEqual(user);
});

test("remove", async () => {
  expect(await remove(user.id)).toEqual(1);
});
