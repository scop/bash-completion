#!/bin/bash -ex

cd ${TMPDIR:-/tmp}

apk upgrade

# Nothing else here, at least yet. Useful this way already in order to
# test some very base executables, as well as ones tha come from
# busybox. Don't lose that if adding stuff here!
