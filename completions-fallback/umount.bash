# umount(8) completion                                     -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.28, use that instead.

if [[ $OSTYPE == *linux* ]]; then
    . "$BASH_SOURCE.linux"
    return
fi

# umount(8) completion. This relies on the mount point being the third
# space-delimited field in the output of mount(8)
#
_comp_cmd_umount()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_split -l -- "$(mount | cut -d" " -f 3)"
} &&
    complete -F _comp_cmd_umount -o dirnames umount

# ex: filetype=sh
