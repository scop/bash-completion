# xhost(1) completion

_comp_cmd_xhost()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    [[ $cur =~ ^[-+] ]]
    local prefix=${BASH_REMATCH-}
    _comp_compgen -P "$prefix" known_hosts
} &&
    complete -F _comp_cmd_xhost xhost
