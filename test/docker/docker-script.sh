#!/bin/sh -ex

if [ $DIST = tools ]; then
    perlcritic helpers/perl
    flake8 helpers/python test test/generate
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

case $DIST in
    centos6|ubuntu14)
        : ${PYTEST:=/root/.local/bin/pytest}
        ;;
    *)
        : ${PYTEST:=pytest-3}
        ;;
esac

cd test
xvfb-run $PYTEST --numprocesses=${PYTEST_NUMPROCESSES:-auto} --dist=loadfile t
xvfb-run ./runCompletion --all --verbose
./runInstall --verbose --all --verbose
./runUnit --all --verbose

cd ..
mkdir install-test
make install DESTDIR=$(pwd)/install-test
