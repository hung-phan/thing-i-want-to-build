import * as EventEmitter from "events";
import { createRedisConnection } from "./redis";

export const eventEmitter = new EventEmitter();
export const pub = createRedisConnection();
export const sub = createRedisConnection();
export const shutdown = () => {
  pub.quit();
  sub.quit();
};
export const createChannel = (clusterID: string): string | never => {
  if (!clusterID) {
    throw new Error(`Invalid clusterID: ${clusterID}`);
  }

  return `WEB_SOCKET_SERVER:${clusterID}`
};
export const publish = (channel: string, value: string): boolean => pub.publish(channel, value);
export const subscribe = (channel, handler: (value: string) => void): void => {
  sub.subscribe(channel);
  eventEmitter.on(channel, handler);
};

sub.on("message", (channel: string, data: string | number) => {
  if (typeof data === "string") {
    eventEmitter.emit(channel, data);
  }
});