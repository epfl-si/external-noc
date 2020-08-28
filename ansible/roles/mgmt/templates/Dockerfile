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

ENV TERM xterm-256color

