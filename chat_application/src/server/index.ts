import * as onDeath from "death";
import { server, shutdown } from "./infrastructure";
import "./application";

server.listen(parseInt(process.env.PORT, 10), () => {
  console.log("Listening on %s", process.env.PORT);
});

onDeath(() => {
  shutdown();
  server.close();
});

