#!/bin/sh -ex

if [ $DIST = tools ]; then
    perlcritic helpers/perl
    flake8 helpers/python
    exit 0
fi

export bashcomp_bash=bash
env

autoreconf -i
./configure
make

make -C completions check

cd test
xvfb-run ./runCompletion --all
./runInstall --all
./runUnit --all

cd ..
mkdir install-test
make install DESTDIR=$(pwd)/install-test
