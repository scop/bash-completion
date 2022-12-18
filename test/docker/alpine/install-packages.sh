#!/bin/bash
set -xeuo pipefail

cd "${TMPDIR:-/tmp}"

apk upgrade

# Nothing much here, at least yet. Useful this way already in order to
# test some very base executables, as well as ones that come from
# busybox. Don't lose that if adding stuff here!

# An arbitrary package containing an init script or the like for
# testing service completion.
apk add nginx-openrc
