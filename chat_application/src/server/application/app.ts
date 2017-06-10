import app from "../infrastructure/app";

app.get("/health", function (req, res) {
  res.send("OK");
});

app.listen(parseInt(process.env.PORT, 10), () => {
  console.log("Listening on %s", process.env.PORT);
});
