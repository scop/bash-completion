#!/bin/sh -ex

if [ "$BSD" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

export bashcomp_bash=bash
env

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTESTFLAGS="--verbose --numprocesses=auto --dist=loadfile"
