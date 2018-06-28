#!/bin/sh -ex

if [ $DIST = tools ]; then
    perlcritic helpers/perl
    flake8 helpers/python test
    exit 0
fi

if [ "$BSD" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

export bashcomp_bash=bash
env

autoreconf -i
./configure
make

make -C completions check

if [ $DIST = centos6 ]; then
    : ${PYTEST:=/root/.local/bin/pytest}
else
    : ${PYTEST:=pytest-3}
fi

cd test
xvfb-run $PYTEST t
xvfb-run ./runCompletion --all --verbose
./runInstall --verbose --all --verbose
./runUnit --all --verbose

cd ..
mkdir install-test
make install DESTDIR=$(pwd)/install-test
