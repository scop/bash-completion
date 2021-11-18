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

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTESTFLAGS="${PYTESTFLAGS---verbose --numprocesses=auto --dist=loadfile}"
cp -p bash-completion-*.tar.* "$oldpwd/"
