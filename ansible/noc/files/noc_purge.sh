#!/bin/bash
#Petit script pour nettoyer tout le binz du NOC
#zf200429.1522

#source: http://patatos.over-blog.com/2016/09/commet-faire-du-menage-dans-les-conteneurs-et-images-docker.html

echo -e "
Arrête le service et enlève le container ET aussi les datas
"

read -p "Etes-vous certain de vouloir tout effacer ?"
read -p "Mais cela va VRAIMENT VRAIMENT tout effacer, y compris les data !"

echo -e "\n\nArrête tous les containers et les efface !\n"
docker rm -f -v traefik blackbox-exporter noc_nodeexporter_1 noc_prometheus_1 noc_pushgateway_1 noc_grafana_1

echo -e "\n\nEfface les images !\n"
docker image rm traefik:1.7 grafana/grafana prom/prometheus prom/pushgateway quay.io/prometheus/node-exporter prom/blackbox-exporter:v0.14.0

echo -e "\n\nEfface les networks !\n"
docker network prune -f

echo -e "\n\nAffiche le résultat !\n"
docker container ls -a
echo -e "\n"
docker image ls
echo -e "\n"
docker volume ls
echo -e "\n"
docker network ls


