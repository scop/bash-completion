FROM ubuntu:14.04

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        dejagnu \
        make \
        tcllib \
        xvfb

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp/

RUN /tmp/install-packages.sh \
    && rm -rf /tmp/install-packages.sh /tmp/cache-buster /var/cache/apt/lists/*
