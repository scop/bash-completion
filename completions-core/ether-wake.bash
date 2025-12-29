# ether-wake(8) completion                                 -*- shell-script -*-

_comp_cmd_ether_wake()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -p)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -u
        _comp_compgen -a -- -W '-V'
        return
    fi

    _comp_compgen_mac_addresses
} &&
    complete -F _comp_cmd_ether_wake ether-wake etherwake

# ex: filetype=sh
