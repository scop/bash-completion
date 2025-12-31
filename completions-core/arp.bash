# arp(8) completion                                        -*- shell-script -*-

_comp_cmd_arp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[iApfHt]*)'
    # shellcheck disable=SC2254
    case $prev in
        --device | -${noargopts}i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        --protocol | -${noargopts}[Ap])
            # TODO protocol/address family
            return
            ;;
        --file | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
        --hw-type | -${noargopts}[Ht])
            # TODO: parse from --help output?
            _comp_compgen -- -W 'ash ether ax25 netrom rose arcnet dlci fddi
                hippi irda x25 eui64'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    local REPLY
    _comp_count_args -a "@(--device|--protocol|--file|--hw-type|-${noargopts}[iApfHt])"
    case $REPLY in
        1)
            local ips=$("$1" -an | command sed -ne \
                's/.*(\([0-9]\{1,3\}\(\.[0-9]\{1,3\}\)\{3\}\)).*/\1/p')
            _comp_compgen -- -W '$ips'
            ;;
        2)
            # TODO if -d mode: "pub"; if not -f mode: hw_addr
            # TODO hw_addr is a configured interface with --use-device/-*D*
            ;;
        3)
            # TODO netmask|pub|temp if -s mode
            ;;
        4)
            # TODO netmask value if previous was "netmask"
            ;;
        5)
            # TODO "pub" if 3rd was "netmask"
            ;;
    esac
} &&
    complete -F _comp_cmd_arp arp

# ex: filetype=sh
