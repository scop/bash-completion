FROM centos:6

RUN sed -i -e /tsflags=nodocs/d /etc/yum.conf \
    && yum -y install \
       https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm \
    && yum -y upgrade \
    && yum -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        /usr/bin/easy_install-3.4 \
        # /usr/bin/which: https://bugzilla.redhat.com/show_bug.cgi?id=1443357 \
        /usr/bin/which \
        /usr/bin/xvfb-run \
        dejagnu \
        tcllib

# Use completions/Makefile.am as cache buster, triggering a fresh
# install of packages whenever it (i.e. the set of possibly tested
# executables) changes.

ADD https://raw.githubusercontent.com/scop/bash-completion/master/completions/Makefile.am \
    https://raw.githubusercontent.com/scop/bash-completion/master/test/requirements.txt \
    install-packages.sh \
    /tmp/

RUN easy_install-3.4 --user pip \
    && /root/.local/bin/pip install --user -Ir /tmp/requirements.txt

RUN /tmp/install-packages.sh \
    && yum -Cy clean all \
    && rm -r /tmp/* /root/.cache/pip
