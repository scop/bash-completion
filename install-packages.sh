#!/bin/bash -ex

cd ${TMPDIR:-/tmp}

shopt -s extglob
export DEBIAN_FRONTEND=noninteractive

dpkg --add-architecture i386  # for wine

apt-get update
apt-get -y upgrade

apt-get -y --no-install-recommends install \
        apt-file \
        curl \
        git \
        software-properties-common

apt-add-repository multiverse

curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get -y --no-install-recommends install \
        nodejs

npm install -g jshint
npm cache clean --force

apt-file update

git clone --depth 1 https://github.com/scop/bash-completion.git

cd bash-completion
autoreconf -i
./configure
make -C completions

excluded=$(cat <<\EOF
arping
bcron-run
evince-gtk
gdb-minimal
gnat-4.6
gnuspool
heimdal
inetutils-ping
knot-host
lpr
lprng
mariadb-client-5.5
mariadb-client-core-5.5
mplayer2
mysql-client-5.5
mysql-client-core-5.5
netscript-2.4
openresolv
percona-xtradb-cluster-client-5.5
postgres-xc-client
python3.5-venv
strongswan-starter
sudo-ldap
xserver-xorg-input-synaptics-lts-utopic
xserver-xorg-input-synaptics-lts-vivid
xserver-xorg-input-synaptics-lts-wily
xserver-xorg-input-synaptics-lts-xenial
EOF
)

for file in completions/!(Makefile*); do
    file=${file##*/}
    printf "%s\n" {/usr,}/{,s}bin/${file#_}
done \
    | apt-file -lFf search - \
    | grep -vF "$excluded" \
    | xargs apt-get -y --no-install-recommends install

# Required but not pulled in by dependencies:
apt-get -y --no-install-recommends install \
    libwww-perl \
    postgresql-client

cd ..
rm -r bash-completion

# Build some *BSD tools for testing

install -dm 755 /usr/local/lib/bsd-bin
apt-get -y --no-install-recommends install bison libbsd-dev subversion

svn co https://svn.freebsd.org/base/release/11.1.0/usr.bin/sed bsd-sed
cd bsd-sed
sed -i -e 's,^__FBSDID.*,#include <bsd/bsd.h>,' *.c
cc -O2 -g -Wall -Wno-unused-const-variable -D_GNU_SOURCE *.c \
   -lbsd -o /usr/local/lib/bsd-bin/sed
cd ..
rm -r bsd-sed

svn co https://svn.freebsd.org/base/release/11.1.0/contrib/one-true-awk
cd one-true-awk
sed -i -e /^__FBSDID/d *.c
make YACC="bison -d -y"
install a.out /usr/local/lib/bsd-bin/awk
cd ..
rm -r one-true-awk
