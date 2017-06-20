# Chat application

Initialize docker environment for local deployment

```bash
eval $(minikube docker-env)
docker build ../apps/chat_application -t chat_application:1.0.0
```

Up
```bash
sh ./chat_application/up.sh
```

Down
```bash
sh ./chat_application/down.sh
```

![alt text](https://raw.githubusercontent.com/hung-phan/thing-i-want-to-build/master/deployer/chat_application.png "chat_application")
