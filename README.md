# iDev-FSD external NOC

# About

This project aims to set up a Network Operations Center (so called
[NOC](https://en.wikipedia.org/wiki/Network_operations_center)) providing an
external monitoring for our School. In short, it will set up
[Prometheus](https://prometheus.io/docs/introduction/overview/), [Prometheus
Pushgateway](https://prometheus.io/docs/practices/pushing/), [Prometheus
Blackbox exporter](https://github.com/prometheus/blackbox_exporter), [Prometheus
Alertmanager](https://prometheus.io/docs/alerting/alertmanager/), [Prometheus
Node Exporter](https://github.com/prometheus/node_exporter) and
[Grafana](https://prometheus.io/docs/visualization/grafana/) on a server, using
docker containers and deployed with [Ansible](https://www.ansible.com). On top
of that, [Traefik](https://traefik.io/) reverse proxy / load balancer handle the
HTTP requests.

# Pre-requisites

We assume that the NOC will be deployed on a Ubuntu server, on which you can
access with your SSH key with the root rights.

## Installation

The installation is self-managed by the `nocsible` script, which will download
the [Ansible suitcase](https://github.com/epfl-si/ansible.suitcase/) if needed.
This will ensure that every member of the team will be using the same versions
of the tools such as python, pip module, ansible modules, ruby, etc.

## Keybase

The secrets in this project are stored on a static yaml file on the team's 
keybase (`keybase/team/epfl_idevfsd/idevfsd-NOC/ansible_noc_secrets.yml`). An 
Ansible file lookup will get them, meaning that access to this file is mandatory 
and that it has to be mounted.

# Deployment

In our case, the deployment in done on a virtual machine hosted on a OpenStack
setup by [SWITCHEngines](https://www.switch.ch/engines/). Thus, some of the
explanations might be related to that, more particularly the access rules which
depends on [OpenStack Neutron Security
Groups](https://wiki.openstack.org/wiki/Neutron/SecurityGroups).

# Project's bricks

Each bricks of the project is meant to be self-contained. It should be possible
to deploy each brick individually, using Ansible tags.

# Usage

## Install
```
$ git clone git@github.com:epfl-si/external-noc.git
$ cd external-noc
$ ./ansible/nocsible --check
```

## Test
```
./ansible/nocsible
```

## Prod
```
./ansible/nocsible --prod
```

# Links
* [Prometheus](https://prometheus.io/docs/introduction/overview/)
  * [Grafana](https://prometheus.io/docs/visualization/grafana/)
  * [Alertmanager](https://prometheus.io/docs/alerting/alertmanager/)
  * [Blackbox exporter](https://github.com/prometheus/blackbox_exporter)
  * [Pushgateway](https://prometheus.io/docs/practices/pushing/)
  * [node_exporter](https://github.com/prometheus/node_exporter)
* [Grafana](https://grafana.com/)
  * [Configuration](http://docs.grafana.org/installation/configuration/)
  * [Docker](http://docs.grafana.org/installation/docker/)
  * [Auth GitHub](http://docs.grafana.org/auth/github/)
  * [Provisionning DataSource](http://docs.grafana.org/administration/provisioning/#example-datasource-config-file)
