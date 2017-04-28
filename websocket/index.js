const WebSocket = require("uws");

const wss = new WebSocket.Server({
  perMessageDeflate: false,
  port: 3000
});

wss.broadcast = function(data) {
  wss.clients.forEach(function(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data);
    }
  });
};

wss.on("connection", function(ws) {
  ws.on("message", function(data) {
    // Broadcast to everyone else.
    wss.clients.forEach(function(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(data);
      }
    });
  });
});