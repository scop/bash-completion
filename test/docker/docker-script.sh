#!/bin/sh -eux

if [ "${BSD-}" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

export bashcomp_bash=bash
env

cp -a . /work
cd /work

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTESTFLAGS="${PYTESTFLAGS---verbose --numprocesses=auto --dist=loadfile}"
