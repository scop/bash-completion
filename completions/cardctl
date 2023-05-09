# Linux cardctl(8) completion                              -*- shell-script -*-

_comp_cmd_cardctl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'status config ident suspend resume reset eject
            insert scheme'
    fi
} &&
    complete -F _comp_cmd_cardctl cardctl pccardctl

# ex: filetype=sh
