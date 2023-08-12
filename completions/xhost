# xhost(1) completion                                      -*- shell-script -*-

_comp_cmd_xhost()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $cur in
        +*) _comp_compgen_known_hosts -p+ -- "${cur:1}" ;;
        -*) _comp_compgen_known_hosts -p- -- "${cur:1}" ;;
        *) _comp_compgen_known_hosts -- "$cur" ;;
    esac
} &&
    complete -F _comp_cmd_xhost xhost

# ex: filetype=sh
