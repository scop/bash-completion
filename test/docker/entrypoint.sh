#!/bin/sh -eux
# shellcheck shell=sh

if [ "${BSD-}" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

export bashcomp_bash=bash
env

oldpwd=$(pwd)
cp -a . /work
cd /work

# Dependencies for running sshd and connecting to it
ssh-keygen -A
mkdir -p ~/.ssh/ /var/run/sshd
echo "localhost $(cat /etc/ssh/ssh_host_ed25519_key.pub)" >>~/.ssh/known_hosts
ssh-keygen -t ed25519 -N '' -f "$HOME/.ssh/id_ed25519"
cat "$HOME/.ssh/id_ed25519.pub" >>"$HOME/.ssh/authorized_keys"

# sshd forces you to run with the full path
sshpath=$(command -v sshd)
$sshpath

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTESTFLAGS="${PYTESTFLAGS---verbose -p no:cacheprovider --numprocesses=auto --dist=loadfile}"
cp -p bash-completion-*.tar.* "$oldpwd/"
sha256sum bash-completion-*.tar.* >"$oldpwd/sha256sums.txt"
