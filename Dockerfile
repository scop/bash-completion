FROM alpine

RUN apk add --no-cache \
        autoconf \
        automake \
        bash \
        dejagnu \
        make \
        python3 \
        xvfb \
        xz \
    && wget -O - https://core.tcl.tk/tcllib/uv/tcllib-1.19.tar.xz | xz -dc | tar xC /tmp \
    && cd /tmp/tcllib-* \
    && ./configure --prefix=/usr \
    && make install-libraries \
    && cd - \
    && : old test suite works with context diffs, n/a with busybox diff \
    && apk add --no-cache diffutils \
    && : no xvfb-run yet, https://bugs.alpinelinux.org/issues/9617 \
    && wget -O /usr/local/bin/xvfb-run https://sources.debian.org/data/main/x/xorg-server/2:1.20.4-1/debian/local/xvfb-run \
    && chmod +x /usr/local/bin/xvfb-run

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    https://raw.githubusercontent.com/scop/bash-completion/master/test/requirements.txt \
    install-packages.sh \
    /tmp/

RUN pip3 install --target /opt/bash-completion-test -Ir /tmp/requirements.txt \
    && echo '#!/bin/sh -e' >/usr/local/bin/pytest \
    && echo 'PYTHONPATH=/opt/bash-completion-test; export PYTHONPATH' \
       >>/usr/local/bin/pytest \
    && echo 'exec /opt/bash-completion-test/bin/pytest "$@"' \
       >>/usr/local/bin/pytest \
    && chmod +x /usr/local/bin/pytest

RUN /tmp/install-packages.sh \
    && rm -r /tmp/* /root/.cache/pip
