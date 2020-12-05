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

# test/test-cmd-list.txt is a cache buster
ADD https://raw.githubusercontent.com/scop/bash-completion/master/test/test-cmd-list.txt \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && rm -r /tmp/*
