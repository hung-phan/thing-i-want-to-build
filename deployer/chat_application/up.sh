#!/usr/bin/env bash

kubectl create -f $(dirname "$0")/redis_deployment.yml
kubectl create -f $(dirname "$0")/redis_service.yml
kubectl create -f $(dirname "$0")/app_deployment.yml
kubectl create -f $(dirname "$0")/app_service.yml
