# Blackbox-exporter
https://github.com/prometheus/blackbox_exporter
`docker run --rm -d -p 9115:9115 --name blackbox_exporter -v `pwd`/blackbox-exporter/config/:/config prom/blackbox-exporter --config.file=/config/blackbox.yml`

https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md
 
## Others links
  * https://www.youtube.com/watch?v=GsozyDTDJvk
  * https://github.com/bitnami/bitnami-docker-blackbox-exporter
  * https://michael.stapelberg.ch/posts/2016-01-01-prometheus-blackbox-exporter/
  * https://medium.com/the-telegraph-engineering/how-prometheus-and-the-blackbox-exporter-makes-monitoring-microservice-endpoints-easy-and-free-of-a986078912ee
