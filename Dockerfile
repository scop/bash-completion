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
        dejagnu \
        tcllib \
    && ln -s $(type -P pytest-3) /usr/local/bin/pytest

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    install-packages.sh \
    /tmp/

RUN /tmp/install-packages.sh \
    && dnf -Cy clean all \
    && rm -r /tmp/*
