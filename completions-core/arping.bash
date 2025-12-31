# arping(8) completion                                     -*- shell-script -*-

_comp_cmd_arping()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*c | -*w)
            return
            ;;
        -*I)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -*s)
            _comp_compgen_ip_addresses
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi

    _comp_compgen_known_hosts -- "$cur"
} &&
    complete -F _comp_cmd_arping arping

# ex: filetype=sh
