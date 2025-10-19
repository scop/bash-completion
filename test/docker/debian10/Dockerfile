FROM debian:10

RUN export DEBIAN_FRONTEND=noninteractive \
    && sed -i -e 's/\<deb\.debian\.org\>/archive.debian.org/' /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        autoconf \
        automake \
        make \
        openssh-server \
        python3-pexpect \
        python3-pytest-xdist \
        xvfb xauth \
    && ln -s $(bash -c "type -P pytest-3") /usr/local/bin/pytest

ADD test-cmd-list.txt \
    docker/debian10/install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh </tmp/test-cmd-list.txt \
    && rm -r /tmp/* /var/lib/apt/lists/*
