(() => {
  "use strict";

  const ws = new WebSocket(`ws://${location.host}`);

  ws.onopen = () => {
    ws.send(JSON.stringify({
      type: "AUTHENTICATION_EVENT",
      payload: {
        id: 1,
        name: "Hung"
      }
    }));
  };

  ws.onmessage = event => {
    console.log(JSON.parse(event.data));
  };
})();
