#!/bin/bash -ex

shopt -s extglob

cd ${TMPDIR:-/tmp}

# upgrade: base image contains vim-minimal, newer vim-* which
# implicitly conflicts with it (typically vim.1.gz) may be in
# repository and pulled in further down, causing install to fail as
# -minimal won't be updated otherwise.
dnf --refresh -y upgrade
dnf -y install /usr/bin/git /usr/bin/xargs
git clone --depth 1 https://github.com/scop/bash-completion.git

cd bash-completion
autoreconf -i
./configure
make -C completions

for file in completions/!(Makefile*); do
    file=${file##*/}
    echo /usr/{,s}bin/${file#_}
# --skip-broken: avoid failing on not found packages. Also prevents actually
# broken packages from failing the install which is not what we want, but
# there doesn't seem to be way to cleanly just skip the not found ones.
done | xargs dnf --skip-broken -y install

cd ..
rm -r bash-completion
