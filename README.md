# iDev-FSD external NOC



## Set up notes
This project aim to finalize some [previous attempts](https://en.wikipedia.org/wiki/Network_operations_center) to set up a Network Operations Center (so called [NOC](https://en.wikipedia.org/wiki/Network_operations_center)) to provide an external monitoring for our School. In short, it will set up [Prometheus](https://prometheus.io/docs/introduction/overview/), [Prometheus Pushgateway](https://prometheus.io/docs/practices/pushing/), [Prometheus Blackbox exporter](https://github.com/prometheus/blackbox_exporter), [Prometheus Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) and [Grafana](https://prometheus.io/docs/visualization/grafana/) from a single `docker-compose.yml` file.

This repository is organized with the [`docker-compose.yml`](docker-compose.yml) a the top and all "docker bricks" under the respective directory. While I tried to stick as much as possible with the default original docker images of each project, some configuration was needed. I've tried to keep things resistant to normal docker cycles and easily backupable if needed. Furthermore, the [`.env`](sample.env) file should highlight the configurable options of the setup ([see this guide on docker arg/env variable](https://vsupalov.com/docker-arg-env-variable-guide/)).









# Links
  * [Grafana](https://prometheus.io/docs/visualization/grafana/)
  * [Prometheus Alertmanager](https://prometheus.io/docs/alerting/alertmanager/)
  * [Prometheus Blackbox exporter](https://github.com/prometheus/blackbox_exporter)
  * [Prometheus Pushgateway](https://prometheus.io/docs/practices/pushing/)
  * [Prometheus node_exporter](https://github.com/prometheus/node_exporter) 
  * [Prometheus](https://prometheus.io/docs/introduction/overview/)