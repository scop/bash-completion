#!/bin/sh -ex

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
