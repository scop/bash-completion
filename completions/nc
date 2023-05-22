# nc(1) completion                                         -*- shell-script -*-

_comp_cmd_nc()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -*[hIiMmOPpqVWw])
            return
            ;;
        -*s)
            if [[ ${words[*]} == *-6* ]]; then
                _comp_compgen_ip_addresses -6
            else
                _comp_compgen_ip_addresses
            fi
            return
            ;;
        -*T)
            _comp_compgen -- -W 'critical inetcontrol lowcost lowdelay
                netcontrol throughput reliability ef af{11..43} cs{0..7}'
            return
            ;;
        -*X)
            _comp_compgen -- -W '4 5 connect'
            return
            ;;
        -*x)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi

    # Complete 1st non-option arg only
    local REPLY
    _comp_count_args -n "" -a "-*[IiMmOPpqsTVWwXx]"
    ((REPLY == 1)) || return

    _comp_compgen_known_hosts -- "$cur"
} &&
    complete -F _comp_cmd_nc nc

# ex: filetype=sh
