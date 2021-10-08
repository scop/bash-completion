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
        tar \
        xvfb \
        xvfb-run \
        xz

# test-cmd-list.txt is just a cache buster here
ADD test-cmd-list.txt \
    docker/alpine/install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && rm -r /tmp/*
