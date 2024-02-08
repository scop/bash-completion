#!/bin/bash
set -xeuo pipefail

cd "${TMPDIR:-/tmp}"

shopt -s extglob
export DEBIAN_FRONTEND=noninteractive

dpkg --add-architecture i386 # for wine

apt-get update
apt-get -y upgrade

apt-get -y --no-install-recommends install \
    apt-file \
    software-properties-common

apt-add-repository contrib
apt-add-repository non-free

apt-get -y --no-install-recommends install \
    npm

npm install -g jshint
npm cache clean --force

apt-file update

excluded=$(
    cat <<\EOF
arping
bcron
bison++
fuse
gdb-minimal
gnat-7
ifupdown
inetutils-ping
lpr
lprng
make-guile
netscript-2.4
ntpsec-ntpdate
openresolv
pkg-config
strongswan-starter
sudo-ldap
systemd-cron
EOF
)

# https://github.com/moby/moby/issues/1297
echo "resolvconf resolvconf/linkify-resolvconf boolean false" |
    debconf-set-selections

# Work around https://bugs.debian.org/1040925
apt-get -y --no-install-recommends install \
    ca-certificates-java

while read -r file; do
    case $file in
        /*) printf "%s\n" "$file" ;;
        *) printf "%s\n" {/usr,}/{,s}bin/"$file" ;;
    esac
done |
    apt-file -lFf search - |
    grep -vF "$excluded" |
    xargs apt-get -y --no-install-recommends install

# Required but not pulled in by dependencies:
apt-get -y --no-install-recommends install \
    postgresql-client

# Build some *BSD tools for testing

apt-get -y --no-install-recommends install \
    build-essential

install -dm 755 /usr/local/lib/bsd-bin
apt-get -y --no-install-recommends install bison libbsd-dev subversion

svn co https://svn.freebsd.org/base/release/11.1.0/usr.bin/sed bsd-sed
cd bsd-sed
sed -i -e 's,^__FBSDID.*,#include <bsd/bsd.h>,' ./*.c
cc -O2 -g -Wall -Wno-unused-const-variable -D_GNU_SOURCE ./*.c \
    -lbsd -o /usr/local/lib/bsd-bin/sed
cd ..
rm -r bsd-sed

svn co https://svn.freebsd.org/base/release/11.1.0/contrib/one-true-awk
cd one-true-awk
sed -i -e /^__FBSDID/d ./*.c
make YACC="bison -d -y"
install a.out /usr/local/lib/bsd-bin/awk
cd ..
rm -r one-true-awk

# Install slapt-get and slapt-src

cd /
curl --fail https://software.jaos.org/slackpacks/slackware64-14.2/slapt-get/slapt-get-0.11.3-x86_64-1.txz |
    tar xvJ
bash -x install/doinst.sh
mkdir -p var/lib/pkgtools/packages # 0.11.3 --available empty without this dir
rm -r install
curl --fail https://software.jaos.org/slackpacks/slackware64-14.2/slapt-src/slapt-src-0.3.6-x86_64-1.txz |
    tar xvJ
bash -x install/doinst.sh
rm -r install
cp -a usr/lib64/* usr/lib/
ln -s libcrypto.so.1.1 usr/lib/x86_64-linux-gnu/libcrypto.so.1
rm -r usr/lib64
cd -
