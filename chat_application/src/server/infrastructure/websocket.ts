import { Server } from "uws";
import * as http from "http";

export default new Server({
  perMessageDeflate: false,
  port: process.env.PORT
});
