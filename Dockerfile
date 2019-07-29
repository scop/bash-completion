FROM debian:10

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        dejagnu \
        make \
        python3-pexpect \
        python3-pytest-xdist \
        tcllib \
        xvfb \
    && ln -s $(bash -c "type -P pytest-3") /usr/local/bin/pytest

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && rm -r /tmp/* /var/lib/apt/lists/*
