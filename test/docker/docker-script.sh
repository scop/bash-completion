#!/bin/sh -ex

if [ $DIST = tools ]; then
    rc=0
    perlcritic helpers/perl; rc=$((rc+1))
    perltidy -nst -nse helpers/perl; rc=$((rc+1))
    if [ -e helpers/perl.ERR ]; then
        cat helpers/perl.ERR
        rc=$((rc+1))
    fi
    flake8 helpers/python test test/generate; rc=$((rc+1))
    black --check -t py27 -t py33 -t py34 -t py35 -t py36 -t py37 -t py38 \
        helpers/python; rc=$((rc+1))
    black --check test test/generate; rc=$((rc+1))
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
