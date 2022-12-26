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

apt-add-repository multiverse

apt-file update

excluded=$(
    cat <<\EOF
arping
bcron-run
bison++
evince-gtk
gdb-minimal
gnat-4.6
gnuspool
heimdal
inetutils-ping
knot-dnsutils
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
    libwww-perl \
    postgresql-client
