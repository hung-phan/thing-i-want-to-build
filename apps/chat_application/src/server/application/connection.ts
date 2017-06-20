import WebSocket from "uws";
import wss from "../infrastructure/websocket";
import User from "../../shared/domain/models/user";
import { create, get, remove } from "../domain/repositories/user";
import { createChannel, publish, subscribe } from "../infrastructure/pubsub";
import {
  AUTHENTICATION_EVENT,
  CHAT_EVENT,
  MessageType
} from "../../shared/domain/models/websocket";

export const connections = {};

wss.on("connection", (client: WebSocket) => {
  client.on("message", async (value: string) => {
    const data: MessageType = JSON.parse(value);

    switch (data.type) {
      case AUTHENTICATION_EVENT:
        await create(
          new User({
            id: data.payload.id,
            name: data.payload.name,
            clusterID: String(process.env.CLUSTER_ID)
          })
        );
        connections[data.payload.id] = client;
        break;

      case CHAT_EVENT:
        client.send(JSON.stringify(data));
        publish(
          createChannel((await get(data.payload.to)).clusterID),
          JSON.stringify(data)
        );
        break;

      default:
        throw new Error(`Invalid message: ${JSON.stringify(data)}`);
    }
  });

  client.on("close", async () => {
    for (const key of Object.keys(connections)) {
      if (connections[key] === client) {
        await remove(connections[key]);
        delete connections[key];
        break;
      }
    }
  });
});

subscribe(createChannel(process.env.CLUSTER_ID), (value: string) => {
  const data: MessageType = JSON.parse(value);

  switch (data.type) {
    case CHAT_EVENT:
      const client: WebSocket = connections[data.payload.to];
      client.send(value);
      break;

    default:
      throw new Error(`Invalid message: ${JSON.stringify(data)}`);
  }
});
