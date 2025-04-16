#!/bin/bash
set -xeuo pipefail

shopt -s extglob

cd "${TMPDIR:-/tmp}"

# upgrade: base image contains vim-minimal, newer vim-* which
# implicitly conflicts with it (typically vim.1.gz) may be in
# repository and pulled in further down, causing install to fail as
# -minimal won't be updated otherwise.
dnf --refresh -y upgrade

dnf -y install /usr/bin/xargs

while read -r file; do
    case $file in
        /*) printf "%s\n" "$file" ;;
        *) printf "%s\n" {/usr,}/{,s}bin/"$file" ;;
    esac
done | grep -vxF /usr/bin/vpnc |
    xargs dnf -y install --skip-unavailable --skip-broken
# /usr/bin/vpnc installs vpnc-consoleuser, which as of 2025-04-16 fails to install in
# rawhide (f42): bugzilla.redhat.com/show_bug.cgi?id=2341517
# --skip-broken: avoid failing on not found packages. Also prevents actually
# broken packages from failing the install which is not what we want, but
# there doesn't seem to be way to cleanly just skip the not found ones.
