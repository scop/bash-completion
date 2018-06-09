#!/bin/bash -ex

shopt -s extglob

cd ${TMPDIR:-/tmp}

yum -y install /usr/bin/git
git clone --depth 1 https://github.com/scop/bash-completion.git

cd bash-completion
autoreconf -i
./configure
make -C completions

for file in completions/!(Makefile*); do
    file=${file##*/}
    echo {/usr,}/{,s}bin/${file#_}
done | xargs yum -y install

cd ..
rm -r bash-completion
