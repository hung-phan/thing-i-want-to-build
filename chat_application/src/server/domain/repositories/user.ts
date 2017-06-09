import User from "../../../domain/models/user";
import { conn } from "../../infrastructure/redis";

export const create = (user: User): Promise<string> =>
  new Promise((resolve, reject) => {
    conn.set(
      `user:${user.id}`,
      JSON.stringify(user),
      (err, result) => (err ? reject(err) : resolve(result))
    );
  });

export const get = (id: string): Promise<User | null> =>
  new Promise((resolve, reject) => {
    conn.get(
      `user:${id}`,
      (err, result) =>
        err
          ? reject(err)
          : resolve(result ? new User(JSON.parse(result)) : result)
    );
  });

export const remove = (id: string): Promise<number> =>
  new Promise((resolve, reject) => {
    conn.del(
      `user:${id}`,
      (err, result) => (err ? reject(err) : resolve(result))
    );
  });
