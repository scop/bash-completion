# pwck(8) completion                                       -*- shell-script -*-

_comp_cmd_pwck()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_pwck pwck

# ex: filetype=sh
