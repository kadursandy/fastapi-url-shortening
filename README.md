
# FastAPI URL Shortening App
### Simplest URl Shortening App

## Features

- POST API - Enter the long url and get the short url
- GET All Shortened URLS
- GET A stored URL with short string

## Installation
```shell
cd fastapi-url-shortener
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 main:app -w 2 -k uvicorn.workers.UvicornWorker --log-level warning
```

## Run using Docker Compose
```shell
cd fastapi-url-shortener
docker-compose build 
docker-compose up -d 
```

## Build and push into docker
```shell
docker build -t kadursandy/fastapi-url-shortener:1.0.0 .
docker run -p 8080:8080 --name fastapi-shortener kadursandy/fastapi-url-shortener:1.0.0
docker login
docker push kadursandy/fastapi-url-shortener:1.0.0
```

## Deploy on Kubernetes
```shell
kubectl create deployment fastapi-url-shortener --replicas=2 --image=kadursandy/fastapi-url-shortener:1.0.0 --port=8080 --dry-run=client -o yaml
kubectl create deployment fastapi-url-shortener --replicas=2 --image=kadursandy/fastapi-url-shortener:1.0.0 --port=8080 --dry-run=client -o yaml > deployment.yml
kubectl create svc loadbalancer fastapi-url-shortener-svc --tcp=8080:8080  --dry-run=client -o yaml > service.yml
kubectl get pods,deploy,svc,hpa
https://betterprogramming.pub/python-fastapi-kubernetes-gcp-296e0dc3abb6
```

#### commands
```shell
kubectl get ns
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl get pods,deploy,svc
```

#### Generate traffic using locust
```shell
locust
```

#### Visualize using istio
<Install Itio|https://istio.io/latest/docs/setup/getting-started/>
https://istio.io/latest/docs/ops/integrations/
```shell
istioctl install
kubectl get ns
kubectl get pod -n kube-system
kubectl get pod -n istio-system
kubectl get ns default --show-labels
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels
kubectl get pod 
kubectl describe pod fastapi-url-shortener-deploy-5b7f9cbd9f-fkrd7

cd ~/istio-practice/istio-1.10.1/samples/addons
kubectl apply -f ~/istio-practice/istio-1.10.1/samples/addons
kubectl get pod -n istio-system
kubectl get svc -n istio-system
kiali
kubectl port-forward svc/kiali -n istio-system 20001

kubectl port-forward svc/prometheus -n istio-system 9411
prometheus
kubectl port-forward svc/prometheus -n istio-system 9090
grafana
kubectl port-forward svc/prometheus -n istio-system 3000

```

```shell
https://github.com/GoogleCloudPlatform/microservices-demo
https://github.com/GoogleCloudPlatform/microservices-demo/blob/master/release/kubernetes-manifests.yaml

```

