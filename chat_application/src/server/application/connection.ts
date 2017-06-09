import WebSocket from "uws";
import server from "../infrastructure/websocket";
import { pub, sub } from "../infrastructure/redis";
import { create, get } from "../domain/repositories/user";
import { AUTHENTICATION_EVENT, CHAT_EVENT, MessageType } from "../../domain/models/websocket";
import User from "../../domain/models/user";

export const createChannel = (clusterID: string) => {
  if (!clusterID) {
    throw new Error(`Invalid clusterID: ${clusterID}`);
  }

  return `WEB_SOCKET_SERVER:${clusterID}`
};

export const connections = {};
export const channel = createChannel(process.env.CLUSTER_ID);

server.on("connection", (client: WebSocket) => {
  client.on("message", async (data: MessageType) => {
    try {
      if (data.type === AUTHENTICATION_EVENT) {
        await create(new User({ ...data.payload, clusterID: process.env.clusterID }));
        connections[data.payload.id] = client;
      } else if (data.type === CHAT_EVENT) {
        pub.publish(createChannel((await get(data.payload.to)).clusterID), data.payload);
      }
    } catch (e) {
      throw new Error("Sth happens");
    }
  });

  client.on("close", () => {
    for (const key of Object.keys(connections)) {
      if (connections[key] === client) {
        delete connections[key];
        break;
      }
    }
  });
});

sub.subscribe(channel);
sub.on("subscribe", (_channel: string, data: MessageType) => {
  if (_channel === channel) {
    switch (data.type) {
      case CHAT_EVENT:
        const client = connections[data.payload.to];
        (<WebSocket>client).send(data.payload);
        break;

      default:
        throw new Error(`Invalid message: ${JSON.stringify(data)}`)
    }
  }
});
