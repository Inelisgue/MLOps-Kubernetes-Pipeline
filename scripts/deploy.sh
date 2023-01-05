#!/bin/bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
echo "Deployment successful"
