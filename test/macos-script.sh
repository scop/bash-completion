#!/bin/sh -eux

# Note that this script is intended to be run only in throwaway environments;
# it may install undesirable things to system locations (if it succeeds in
# that).

brew install \
    automake \
    bash

python3 -m pip install -r test/requirements.txt

export bashcomp_bash=bash
env

autoreconf -i
./configure
make -j

make distcheck \
    PYTESTFLAGS="${PYTESTFLAGS---verbose --numprocesses=auto --dist=loadfile}"
cp -p bash-completion-*.tar.* "$oldpwd/"
