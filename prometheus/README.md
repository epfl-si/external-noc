# Prometheus

## Manual commands
docker run -d -p 9090:9090 --name=idevfsd-prometheus -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus


docker run -d -p 9091:9091 --name=idevfsd-push-gateway prom/pushgateway