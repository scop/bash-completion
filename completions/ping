# ping(8) completion                                       -*- shell-script -*-

_comp_cmd_ping()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    local ipvx

    case $prev in
        -*[cFGghilmPpstVWwz])
            return
            ;;
        -*I)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -*M)
            # Path MTU strategy in Linux, mask|time in FreeBSD
            local opts="do want dont"
            [[ $OSTYPE == *bsd* ]] && opts="mask time"
            _comp_compgen -- -W '$opts'
            return
            ;;
        -*N)
            if [[ $cur != *= ]]; then
                _comp_compgen -- -W 'name ipv6 ipv6-global ipv6-sitelocal
                    ipv6-linklocal ipv6-all ipv4 ipv4-all subject-ipv6=
                    subject-ipv4= subject-name= subject-fqdn='
                [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            fi
            return
            ;;
        -*Q)
            # TOS in Linux, "somewhat quiet" (no args) in FreeBSD
            if [[ $OSTYPE != *bsd* ]]; then
                _comp_compgen -- -W '{0..7}'
                return
            fi
            ;;
        -*S)
            # Socket sndbuf in Linux, source IP in FreeBSD
            [[ $OSTYPE == *bsd* ]] && _comp_compgen_ip_addresses
            return
            ;;
        -*T)
            # Timestamp option in Linux, TTL in FreeBSD
            [[ $OSTYPE == *bsd* ]] ||
                _comp_compgen -- -W 'tsonly tsandaddr'
            return
            ;;
        -*4*)
            ipvx=-4
            ;;
        -*6*)
            ipvx=-6
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    [[ $1 == *6 ]] && ipvx=-6
    [[ $1 == *4 ]] && ipvx=-4
    _comp_compgen_known_hosts ${ipvx-} -- "$cur"
} &&
    complete -F _comp_cmd_ping ping ping4 ping6

# ex: filetype=sh
