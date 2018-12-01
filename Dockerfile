FROM ubuntu:14.04

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        dejagnu \
        make \
        python3-pip \
        tcllib \
        xvfb \
    && pip3 install --ignore-installed --user pytest-xdist pexpect typing

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp/

RUN /tmp/install-packages.sh \
    && rm -rf /tmp/* /var/cache/apt/lists/*
