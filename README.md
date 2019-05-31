# iDev-FSD external NOC

<!-- TOC titleSize:2 tabSpaces:3 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 -->

## Table of Contents
- [iDev-FSD external NOC](#idev-fsd-external-noc)
- [About](#about)
- [Pre-requisites](#pre-requisites)
- [Deployment](#deployment)
- [Project's bricks](#projects-bricks)
   - [Prometheus & Blackbox exporter](#prometheus-blackbox-exporter)
   - [Grafana](#grafana)
   - [Traefik](#traefik)
- [Links](#links)

<!-- /TOC -->

# About

This project aims to set up a Network Operations Center (so called
[NOC](https://en.wikipedia.org/wiki/Network_operations_center)) providing an
external monitoring for our School. In short, it will set up
[Prometheus](https://prometheus.io/docs/introduction/overview/), [Prometheus
Pushgateway](https://prometheus.io/docs/practices/pushing/), [Prometheus
Blackbox exporter](https://github.com/prometheus/blackbox_exporter), [Prometheus
Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) and
[Grafana](https://prometheus.io/docs/visualization/grafana/) on a server, using
docker containers and deployed with [Ansible](https://www.ansible.com).

# Pre-requisites

We assume that the NOC will be deployed on a Ubuntu server, on which you can 
access with your SSH key with the root rights. Ansible is needed on the machine
you are using to deploy. As the secret are hidden using `eyaml`, you will also 
need it on your machine.

// @TODO: List all the pre-requisites and the commands to install them 

# Deployment
In our case, the deployment in done on a virtual machine hosted on a OpenStack
setup by [SWITCHEngines](https://www.switch.ch/engines/). Thus, some of the
explanations might be related to that, more particularly the access rules which
depends on [OpenStack Neutron Security
Groups](https://wiki.openstack.org/wiki/Neutron/SecurityGroups).

# Project's bricks

## Prometheus & Blackbox exporter
Prometheus configuration stands in the
[`prometheus/prometheus.yml`](prometheus/prometheus.yml) file. The Blackbox 
exporter is used to probe some URLs which are defined in the config file. You 
may need to understand how the [Blackbox exporter 
modules](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md#module),
defined in 
[`blackbox-exporter/config/blackbox.yml`](blackbox-exporter/config/blackbox.yml) 
work in order to define new
[scrape_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) 
for Prometheus. The Blackbox exporter allow probing of endpoints over HTTP, 
HTTPS, DNS, TCP and ICMP.

## Grafana

## Traefik


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
    
