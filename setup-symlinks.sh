#!/bin/sh -eu

targetdir="$1"
shift
target="$1"
shift

for file in "$@"; do
    rm -f "$targetdir/$file"
    ln -s "$target" "$targetdir/$file"
done
