FROM fedora:rawhide

RUN echo install_weak_deps=False >> /etc/dnf/dnf.conf \
    && sed -i -e /tsflags=nodocs/d /etc/dnf/dnf.conf \
    && dnf -y --refresh upgrade \
    && dnf -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        /usr/bin/xvfb-run \
        /usr/bin/pytest-3 \
        python3-pexpect \
        python3-pytest-xdist \
    && ln -s $(type -P pytest-3) /usr/local/bin/pytest

# test/test-cmd-list.txt is a cache buster
ADD https://raw.githubusercontent.com/scop/bash-completion/master/test/test-cmd-list.txt \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && dnf -Cy clean all \
    && rm -r /tmp/* /var/lib/dnf/history.sqlite* /var/lib/dnf/repos/*
