FROM centos:7

RUN set -x \
    && sed -i -e /tsflags=nodocs/d /etc/yum.conf \
    && yum -y install \
       https://dl.fedoraproject.org/pub/archive/epel/7/x86_64/Packages/e/epel-release-7-14.noarch.rpm \
    && sed -i \
           -e 's/^mirrorlist/#mirrorlist/' \
           -e 's/mirror\.centos\.org/vault.centos.org/' \
           -e 's|^#\(baseurl=http.*/vault\)|\1|' \
       /etc/yum.repos.d/*.repo \
    && yum -y upgrade \
    && yum -y install \
        /usr/bin/autoconf \
        /usr/bin/automake \
        /usr/bin/make \
        # /usr/bin/which: https://bugzilla.redhat.com/show_bug.cgi?id=1443357 \
        /usr/bin/which \
        /usr/bin/xvfb-run \
        openssh-server \
        python36-pexpect

ADD test-cmd-list.txt \
    requirements.txt \
    docker/centos7/install-packages.sh \
    /tmp/

RUN set -x \
    && pip3 install --prefix /usr/local -Ir /tmp/requirements.txt

RUN /tmp/install-packages.sh </tmp/test-cmd-list.txt \
    && yum -Cy clean all \
    && rm -r /tmp/* /root/.cache/pip /var/lib/yum/history/* /var/lib/yum/yumdb/*
