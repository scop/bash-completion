#!/bin/sh -ex

if [ $DIST = tools ]; then
    rc=0
    perlcritic helpers/perl; rc=$((rc+$?))
    perltidy -nst -nse helpers/perl; rc=$((rc+$?))
    if [ -e helpers/perl.ERR ]; then
        cat helpers/perl.ERR
        rc=$((rc+1))
    fi
    flake8 helpers/python test test/generate; rc=$((rc+$?))
    black --check -t py27 -t py33 -t py34 -t py35 -t py36 -t py37 -t py38 \
        helpers/python; rc=$((rc+$?))
    black --check test test/generate; rc=$((rc+$?))
    exit $rc
fi

if [ "$BSD" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

case $DIST in
    alpine|centos6|ubuntu14)
        : ${PYTEST:=/root/.local/bin/pytest}
        ;;
    *)
        : ${PYTEST:=pytest-3}
        ;;
esac

export bashcomp_bash=bash
env

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTEST=$PYTEST \
    PYTESTFLAGS="--numprocesses=auto --dist=loadfile" \
    RUNTESTFLAGS="--all --verbose"
