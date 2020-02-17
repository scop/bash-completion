#!/bin/sh -ex

if [ $DIST = tools ]; then
    rc=0
    perlcritic helpers/perl; rc=$((rc+$?))
    perltidy -nst -nse helpers/perl; rc=$((rc+$?))
    if [ -e helpers/perl.ERR ]; then
        cat helpers/perl.ERR
        rc=$((rc+1))
    fi
    pre-commit run --all-files; rc=$((rc+$?))
    exit $rc
fi

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
    PYTESTFLAGS="--numprocesses=auto --dist=loadfile" \
    RUNTESTFLAGS="--all --verbose"
