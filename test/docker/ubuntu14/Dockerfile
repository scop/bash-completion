FROM ubuntu:14.04

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        make \
        software-properties-common \
        openssh-server \
        xvfb \
    && : 20250517/3.13.3+20250517 was latest found working as of 2025-10-12 \
    && python3.4 -c "import urllib.request; urllib.request.urlretrieve('https://github.com/astral-sh/python-build-standalone/releases/download/20250517/cpython-3.13.3+20250517-x86_64_v2-unknown-linux-gnu-install_only_stripped.tar.gz', '/tmp/python.tar.gz')" \
    && tar xCf /usr/local /tmp/python.tar.gz --strip-components=1

ADD test-cmd-list.txt \
    requirements.txt \
    docker/ubuntu14/install-packages.sh \
    /tmp/

RUN set -x \
    && python3 -m pip install -Ir /tmp/requirements.txt

RUN /tmp/install-packages.sh </tmp/test-cmd-list.txt \
    && rm -r /tmp/* /root/.cache/pip /var/lib/apt/lists/*
