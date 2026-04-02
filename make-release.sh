#!/bin/sh -eux
# shellcheck shell=sh

autoreconf -i
./configure
# TODO: Consider using the already created and tested tarball from the CI
# workflow
make distcheck
