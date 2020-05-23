FROM centos:7

RUN set -x \
    && sed -i -e /tsflags=nodocs/d /etc/yum.conf \
    && yum -y install \
       https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum -y upgrade \
    && yum -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        # /usr/bin/which: https://bugzilla.redhat.com/show_bug.cgi?id=1443357 \
        /usr/bin/which \
        /usr/bin/xvfb-run \
        python36-pexpect

# test/test-cmd-list.txt is a cache buster
ADD https://raw.githubusercontent.com/scop/bash-completion/master/test/test-cmd-list.txt \
    https://raw.githubusercontent.com/scop/bash-completion/master/test/requirements.txt \
    install-packages.sh \
    /tmp/

RUN set -x \
    && pip3 install --user -Ir /tmp/requirements.txt \
    && echo '#!/bin/sh -e' >/usr/local/bin/pytest \
    && echo 'exec $HOME/.local/bin/pytest "$@"' >>/usr/local/bin/pytest \
    && chmod +x /usr/local/bin/pytest

RUN /tmp/install-packages.sh \
    && yum -Cy clean all \
    && rm -r /tmp/* /root/.cache/pip
