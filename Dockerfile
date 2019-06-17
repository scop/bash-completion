FROM ubuntu:14.04

# Distro's python3-pip is too old to understand environment markers in
# requirements.txt, therefore installing pip from PyPI too, using
# easy_install3 from python3-setuptools.

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        dejagnu \
        make \
        python3-setuptools \
        tcllib \
        xvfb

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    https://raw.githubusercontent.com/scop/bash-completion/master/test/requirements.txt \
    install-packages.sh \
    /tmp/

RUN easy_install3 --user pip \
    && /root/.local/bin/pip install \
       --target /opt/bash-completion-test -Ir /tmp/requirements.txt \
    && echo '#!/bin/sh -e' >/usr/local/bin/pytest \
    && echo 'PYTHONPATH=/opt/bash-completion-test; export PYTHONPATH' \
       >>/usr/local/bin/pytest \
    && echo 'exec /opt/bash-completion-test/bin/pytest "$@"' \
       >>/usr/local/bin/pytest \
    && chmod +x /usr/local/bin/pytest

RUN /tmp/install-packages.sh \
    && rm -r /tmp/* /root/.cache/pip /var/lib/apt/lists/*
