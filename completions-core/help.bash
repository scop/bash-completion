# bash completion for help                                 -*- shell-script -*-

_comp_cmd_help()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -c help -s "$1"
        return
    fi

    _comp_compgen -- -A helptopic
    ((${#COMPREPLY[*]} != 1)) || printf -v "COMPREPLY[0]" %q "$COMPREPLY"
} &&
    complete -F _comp_cmd_help help
