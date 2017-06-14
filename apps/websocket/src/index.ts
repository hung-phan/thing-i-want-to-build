const socket = new WebSocket("ws://localhost:3000");
const $app = <HTMLElement> document.querySelector("#app");
const $input = <HTMLInputElement> document.querySelector("#input");
const $button = <HTMLButtonElement> document.querySelector("#button");

// Connection opened
socket.addEventListener("open", () => {
  console.log("Open ws connection");
});

// Listen for messages
socket.addEventListener("message", (event) => {
  $app.innerHTML = `${$app.innerHTML}<div>${event.data}</div>`;
});

const eventHandler = () => {
  $app.innerHTML = `${$app.innerHTML}<div>${$input.value}</div>`;
  socket.send($input.value);
  $input.value = "";
};

$button.addEventListener("click", eventHandler);
$input.addEventListener("keyup", (event) => {
  if (event.code === "Enter") {
    eventHandler();
  }
});