# mailman genaliases completion                            -*- shell-script -*-

_comp_cmd_genaliases()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--quiet --help'
    fi

} &&
    complete -F _comp_cmd_genaliases genaliases

# ex: filetype=sh
