# mailman unshunt completion                               -*- shell-script -*-

_comp_cmd_unshunt()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen_filedir -d
    fi

} &&
    complete -F _comp_cmd_unshunt unshunt

# ex: filetype=sh
