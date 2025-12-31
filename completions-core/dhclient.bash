# bash completion for dhclient                             -*- shell-script -*-

_comp_cmd_dhclient()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -p | -e)
            return
            ;;
        -D)
            _comp_compgen -- -W 'LL LLT'
            return
            ;;
        -*f)
            _comp_compgen_filedir
            return
            ;;
        -s)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    else
        _comp_compgen_available_interfaces
    fi
} &&
    complete -F _comp_cmd_dhclient dhclient

# ex: filetype=sh
