# sshmitm completion                                       -*- shell-script -*-

_comp_cmd_sshmitm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    else
        _comp_compgen_known_hosts -- "$cur"
    fi

} &&
    complete -F _comp_cmd_sshmitm sshmitm

# ex: filetype=sh
