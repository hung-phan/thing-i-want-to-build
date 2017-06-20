#!/usr/bin/env bash

kubectl delete service application
kubectl delete service redis
kubectl delete deployment application
kubectl delete deployment redis
