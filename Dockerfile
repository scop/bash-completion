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
        dejagnu \
        tcllib

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp

RUN /tmp/install-packages.sh \
    && rm /tmp/install-packages.sh /tmp/cache-buster \
    && dnf -Cy clean all
