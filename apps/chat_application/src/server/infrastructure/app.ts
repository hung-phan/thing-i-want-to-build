import * as express from "express";

const app = express();
app.set("view engine", "pug");
app.set("views", "./src/server/application/templates");

export default app;
