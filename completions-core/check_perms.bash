# mailman check_perms completion                           -*- shell-script -*-

_comp_cmd_check_perms()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-f -v -h'
    fi

} &&
    complete -F _comp_cmd_check_perms check_perms

# ex: filetype=sh
