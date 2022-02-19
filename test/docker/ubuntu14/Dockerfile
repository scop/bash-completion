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
    && python3.4 -c "import urllib.request; urllib.request.urlretrieve('https://github.com/pyston/pyston/releases/download/pyston_2.3.1/pyston_2.3.1_portable_v2.tar.gz', '/tmp/pyston.tar.gz')" \
    && tar xCf /usr/local /tmp/pyston.tar.gz --strip-components=1

ADD test-cmd-list.txt \
    requirements.txt \
    docker/ubuntu14/install-packages.sh \
    /tmp/

RUN set -x \
    && pyston3 -m pip install -Ir /tmp/requirements.txt

RUN /tmp/install-packages.sh </tmp/test-cmd-list.txt \
    && rm -r /tmp/* /root/.cache/pip /var/lib/apt/lists/*
