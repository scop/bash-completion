FROM alpine

RUN apk add --no-cache \
        autoconf \
        automake \
        bash \
        gcc \
        make \
        musl-dev \
        py3-pexpect \
        py3-pytest-xdist \
        xvfb \
        xvfb-run \
        xz

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && rm -r /tmp/*
