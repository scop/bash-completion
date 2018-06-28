FROM centos:6

RUN sed -i -e /tsflags=nodocs/d /etc/yum.conf \
    && yum -y install \
       https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
       https://centos6.iuscommunity.org/ius-release.rpm \
    && yum -y upgrade \
    && yum -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        /usr/bin/pip3.6 \
        # /usr/bin/which: https://bugzilla.redhat.com/show_bug.cgi?id=1443357 \
        /usr/bin/which \
        /usr/bin/xvfb-run \
        dejagnu \
        tcllib \
    && pip3.6 install --ignore-installed --user pytest pexpect

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am /tmp/cache-buster
COPY install-packages.sh /tmp

RUN /tmp/install-packages.sh \
    && rm /tmp/install-packages.sh /tmp/cache-buster \
    && yum -Cy clean all \
    && rm -r /root/.cache/pip
