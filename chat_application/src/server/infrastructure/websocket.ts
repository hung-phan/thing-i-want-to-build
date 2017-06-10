import { Server } from "uws";
import server from "./server";

export default new Server({
  server,
  perMessageDeflate: false
});
