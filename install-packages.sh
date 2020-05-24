#!/bin/bash -ex

shopt -s extglob

cd ${TMPDIR:-/tmp}

yum -y install /usr/bin/git
git clone --depth 1 https://github.com/scop/bash-completion.git

while read -r file; do
    case $file in
        mock | */mock) printf "%s\n" mock ;;
        /*) printf "%s\n" "$file" ;;
        *)  printf "%s\n" {/usr,}/{,s}bin/"$file" ;;
    esac
done < bash-completion/test/test-cmd-list.txt \
| xargs yum -y install

rm -r bash-completion
