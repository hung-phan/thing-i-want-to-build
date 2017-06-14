(() => {
  "use strict";

  const ws = new WebSocket(`ws://${location.host}`);

  ws.onopen = () => {
    ws.send(JSON.stringify({
      type: "AUTHENTICATION_EVENT",
      payload: {
        id: 2,
        name: "Nghi"
      }
    }));

    ws.send(JSON.stringify({
      type: "CHAT_EVENT",
      payload: {
        from: 2,
        to: 1,
        content: "Hello from the other side"
      }
    }));
  };

  ws.onmessage = event => {
    console.log(JSON.parse(event.data));
  };
})();
