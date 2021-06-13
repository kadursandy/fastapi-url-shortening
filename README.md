
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