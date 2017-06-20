import app from "../infrastructure/app";

app.get("/health", (req, res) => {
  res.send("OK");
});

app.get("/", (req, res) => {
  res.render("index", { cluster: process.env.CLUSTER_ID });
});
