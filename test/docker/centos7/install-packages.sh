#!/bin/bash
set -xeuo pipefail

shopt -s extglob

cd "${TMPDIR:-/tmp}"

while read -r file; do
    case $file in
        mock | */mock) printf "%s\n" mock ;;
        /*) printf "%s\n" "$file" ;;
        *) printf "%s\n" {/usr,}/{,s}bin/"$file" ;;
    esac
done |
    xargs yum -y install
