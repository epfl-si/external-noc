FROM "{{ mgmt_image }}:{{ mgmt_version }}"
LABEL maintainer="idev-fsd@groupes.epfl.ch"

RUN apt-get -qy update && apt-get -qy install --no-install-recommends \
    bash-completion \
    curl \
    htop \
    iputils-arping \
    iputils-ping \
    less \
    make \
    openssl \
    pwgen \
    software-properties-common \
    telnet \
    tmux \
    tree \
    wget \
    zsh \
  && \
    apt-get -qy autoremove && \
    apt-get clean
