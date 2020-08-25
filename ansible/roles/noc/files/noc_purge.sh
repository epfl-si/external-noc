#!/bin/bash
# Small script to clean all the NOC binz
# source: http://patatos.over-blog.com/2016/09/commet-faire-du-menage-dans-les-conteneurs-et-images-docker.html

echo -e "
Stop the service and remove the container AND also the data"

read -p "Are you sure you want to erase everything ?"
read -p "But this will REALLY REALLY erase everything, including the data !"

echo -e "\n\nStop all the containers and erase them !\n"
docker rm -f -v traefik blackbox-exporter noc_nodeexporter_1 noc_prometheus_1 noc_pushgateway_1 noc_grafana_1

echo -e "\n\nErase the images !\n"
docker image rm traefik:1.7 grafana/grafana prom/prometheus prom/pushgateway quay.io/prometheus/node-exporter prom/blackbox-exporter:v0.14.0

echo -e "\n\nErase the networks !\n"
docker network prune -f

echo -e "\n\nShow the result !\n"
docker container ls -a
echo -e "\n"
docker image ls
echo -e "\n"
docker volume ls
echo -e "\n"
docker network ls


