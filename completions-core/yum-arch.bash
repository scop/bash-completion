# yum-arch(8) completion                                   -*- shell-script -*-

_comp_cmd_yum_arch()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-d -v -vv -n -c -z -s -l -q'
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_yum_arch yum-arch

# ex: filetype=sh
