FROM "{{ mgmt_image }}:{{ mgmt_version }}"
LABEL maintainer="idev-fsd@groupes.epfl.ch"

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=Europe/Zurich

RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    bash-completion \
    curl \
    git \
    htop \
    iputils-arping \
    iputils-ping \
    jq \
    less \
    make \
    net-tools \
    openssl \
    pwgen \
    software-properties-common \
    telnet \
    tmux \
    tree \
    vim \
    wget \
  && \
    apt-get -qy autoremove && \
    apt-get clean

# Install promtool
RUN curl -sL https://api.github.com/repos/prometheus/prometheus/releases/latest | jq -r '.assets[].browser_download_url' | grep linux-amd64 | wget -O prometheus-latest.tar.gz -i -
RUN tar -zxvf prometheus-latest.tar.gz --wildcards */promtool && rm prometheus-latest.tar.gz
RUN mv */promtool /usr/local/bin/ && chmod +x /usr/local/bin/promtool

ENV TERM xterm-256color

