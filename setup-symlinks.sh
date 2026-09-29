#!/bin/sh -eu

targetdir=$1
shift
target=$1
shift

for file in "$@"; do
    rm -f "$targetdir/$file" "$targetdir/_$file" "$targetdir/$file.bash"
    ln -s "$target.bash" "$targetdir/$file.bash"
done
