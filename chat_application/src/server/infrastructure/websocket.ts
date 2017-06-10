import { Server } from "uws";
import * as http from "http";
import app from "./app";

export default new Server({
  server: http.createServer(app),
  perMessageDeflate: false
});
