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

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && rm -r /tmp/* /root/.cache/pip /var/lib/apt/lists/*
