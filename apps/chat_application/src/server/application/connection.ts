import WebSocket from "uws";
import wss from "../infrastructure/websocket";
import User from "../../shared/domain/models/user";
import { create, get } from "../domain/repositories/user";
import { createChannel, publish, subscribe } from "../infrastructure/pubsub";
import { AUTHENTICATION_EVENT, CHAT_EVENT, MessageType } from "../../shared/domain/models/websocket";

const connections = {};

wss.on("connection", (client: WebSocket) => {
  client.on("message", async (value: string) => {
    const data: MessageType = JSON.parse(value);

    switch (data.type) {
      case AUTHENTICATION_EVENT:
        await create(new User({ ...data.payload, clusterID: process.env.CLUSTER_ID }));
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
        throw new Error(`Invalid message: ${JSON.stringify(data)}`)
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

subscribe(createChannel(process.env.CLUSTER_ID), (value: string) => {
  const data: MessageType = JSON.parse(value);

  switch (data.type) {
    case CHAT_EVENT:
      const client = connections[data.payload.to];
      (<WebSocket>client).send(JSON.stringify(data));
      break;

    default:
      throw new Error(`Invalid message: ${JSON.stringify(data)}`)
  }
});
