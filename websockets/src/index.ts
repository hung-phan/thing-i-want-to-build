const socket = new WebSocket('ws://localhost:3000');
const appElement = document.querySelector("#app");

// Connection opened
socket.addEventListener('open', function () {
  socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
  appElement.innerHTML = `${appElement.innerHTML}<div>${event.data}</div>`;
});