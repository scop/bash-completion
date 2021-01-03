FROM ubuntu:14.04

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        make \
        software-properties-common \
        xvfb \
    && apt-add-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        python3.6 \
    && python3.6 -c "import urllib.request; urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', '/tmp/get-pip.py')" \
    && python3.6 /tmp/get-pip.py --prefix /usr/local

# test/test-cmd-list.txt is a cache buster
ADD https://raw.githubusercontent.com/scop/bash-completion/master/test/test-cmd-list.txt \
    https://raw.githubusercontent.com/scop/bash-completion/master/test/requirements.txt \
    install-packages.sh \
    /tmp/

RUN set -x \
    && python3.6 -m pip install --prefix /usr/local -Ir /tmp/requirements.txt

RUN /tmp/install-packages.sh \
    && rm -r /tmp/* /root/.cache/pip /var/lib/apt/lists/*
