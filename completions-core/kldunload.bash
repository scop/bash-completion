# FreeBSD kldunload completion                             -*- shell-script -*-

[[ $OSTYPE == *freebsd* ]] || return 1

_comp_cmd_kldunload()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_split -X '!*.ko' -- "$(kldstat)" &&
        COMPREPLY=("${COMPREPLY[@]%.ko}")
} &&
    complete -F _comp_cmd_kldunload kldunload

# ex: filetype=sh
