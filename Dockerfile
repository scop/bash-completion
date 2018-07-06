FROM centos:6

RUN sed -i -e /tsflags=nodocs/d /etc/yum.conf \
    && yum -y install \
       https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
    && yum -y upgrade \
    && yum -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        /usr/bin/python3 \
        # /usr/bin/which: https://bugzilla.redhat.com/show_bug.cgi?id=1443357 \
        /usr/bin/which \
        /usr/bin/xvfb-run \
        dejagnu \
        tcllib \
    && $(ls /usr/bin/easy_install-3* | head -n 1) pip \
    && pip3 install --ignore-installed --user pytest pexpect typing

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp

RUN /tmp/install-packages.sh \
    && rm /tmp/install-packages.sh /tmp/cache-buster \
    && yum -Cy clean all \
    && rm -r /root/.cache/pip
