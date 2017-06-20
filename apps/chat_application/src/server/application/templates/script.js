(() => {
  "use strict";
  const ws = new WebSocket(`ws://${location.host}`);
  const createUserPanelElement = document.getElementById("create-user-panel");
  const createUserPanelIdElement = document.getElementById("create-user-panel__id");
  const createUserPanelNameElement = document.getElementById("create-user-panel__name");
  const chatPanelElement = document.getElementById("chat-panel");
  const chatPanelContentElement = document.getElementById("chat-panel__content");
  const chatPanelToElement = document.getElementById("chat-panel__to");
  const chatPanelMessageElement = document.getElementById("chat-panel__message");
  let id;

  window.createUser = () => {
    id = createUserPanelIdElement.value;
    ws.send(JSON.stringify({
      type: "AUTHENTICATION_EVENT",
      payload: {
        id,
        name: createUserPanelNameElement.value
      }
    }));
    createUserPanelElement.style.display = "none";
    chatPanelElement.style.display = "block";
  };

  window.appendMessage = (payload) => {
    chatPanelContentElement
      .insertAdjacentHTML(
        "beforeend",
        `<div><b>${payload.from}: </b>${payload.content}</div>`
      );
  };

  window.sendMessage = () => {
    ws.send(JSON.stringify({
      type: "CHAT_EVENT",
      payload: {
        from: id,
        to: chatPanelToElement.value,
        content: chatPanelMessageElement.value
      }
    }));
    chatPanelMessageElement.value = "";
  };

  ws.onmessage = event => {
    const { type, payload } = JSON.parse(event.data);

    if (type === "CHAT_EVENT") {
      window.appendMessage(payload);
    }
  };
})();
