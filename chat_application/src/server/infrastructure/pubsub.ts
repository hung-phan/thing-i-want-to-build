import * as redis from "redis";
import * as EventEmitter from "events";

const eventEmitter = new EventEmitter();
const pub = redis.createClient();
const sub = redis.createClient();

export const createChannel = (clusterID: string): string | never => {
  if (!clusterID) {
    throw new Error(`Invalid clusterID: ${clusterID}`);
  }

  return `WEB_SOCKET_SERVER:${clusterID}`
};
export const publish = (channel: string, value: any): boolean => pub.publish(channel, value);
export const subscribe = (channel, handler: (value: any) => void): void => {
  sub.subscribe(channel);
  eventEmitter.on(channel, handler)
};

sub.on("subscribe", (channel: string, data: any) => eventEmitter.emit(channel, data));

for (const event of ["exit", "SIGINT", "uncaughtException"]) {
  process.on(event, () => {
    eventEmitter.removeAllListeners();
    sub.unsubscribe();

    pub.quit();
    sub.quit();
  });
}
