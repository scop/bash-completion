#!/bin/sh -eux

# Note that this script is intended to be run only in throwaway environments;
# it may install undesirable things to system locations (if it succeeds in
# that).

brew install \
    automake \
    bash

python3 -m venv venv
#shellcheck disable=SC1091
source venv/bin/activate
python3 -m pip install -r test/requirements.txt

export bashcomp_bash=bash
env
LC_ALL=C sort <<<$'python-dev\npython3-dev'
LC_COLLATE=C sort <<<$'python-dev\npython3-dev'
LC_ALL=en_US.UTF-8 sort <<<$'python-dev\npython3-dev'
LC_COLLATE=en_US.UTF-8 sort <<<$'python-dev\npython3-dev'


autoreconf -i
./configure
make -j

make distcheck \
    PYTESTFLAGS="${PYTESTFLAGS---verbose -p no:cacheprovider --numprocesses=auto --dist=loadfile}"
