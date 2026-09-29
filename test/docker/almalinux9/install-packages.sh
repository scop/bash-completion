#!/bin/bash
set -xeuo pipefail

shopt -s extglob

cd "${TMPDIR:-/tmp}"

while read -r file; do
    case $file in
        /*) printf "%s\n" "$file" ;;
        *) printf "%s\n" {/usr,}/{,s}bin/"$file" ;;
    esac
done |
    xargs dnf -y install --skip-broken
# --skip-broken: avoid failing on not found packages. Also prevents actually
# broken packages from failing the install which is not what we want, but
# there doesn't seem to be way to cleanly just skip the not found ones.
