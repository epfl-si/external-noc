# Kuma

## About

Uptime Kuma is an easy-to-use self-hosted monitoring tool, similar to uptime 
robot but free and open source.

## Install notes

- https://github.com/louislam/uptime-kuma
- https://hub.docker.com/r/louislam/uptime-kuma

```sh
docker run -d \
  --restart=always \
  -p 3001:3001 \
  -v uptime-kuma:/app/data \
  --name uptime-kuma \
  louislam/uptime-kuma:1
```
