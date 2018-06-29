FROM ubuntu:14.04

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        dejagnu \
        make \
        software-properties-common \
        tcllib \
        xvfb \
    && apt-add-repository --yes ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        curl \
        python3.6 \
    && curl https://bootstrap.pypa.io/get-pip.py | python3.6 \
    && pip3.6 install --ignore-installed --user pytest pexpect

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp/

RUN /tmp/install-packages.sh \
    && rm -rf /tmp/install-packages.sh /tmp/cache-buster /var/cache/apt/lists/*
