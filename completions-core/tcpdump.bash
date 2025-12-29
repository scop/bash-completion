# bash completion for tcpdump                              -*- shell-script -*-

_comp_cmd_tcpdump()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[rwFVimTzZBcCDEGMsWyjQ]*)'
    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}[rwFV])
            _comp_compgen_filedir
            return
            ;;
        --interface | -${noargopts}i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -${noargopts}m)
            _comp_compgen_filedir mib
            return
            ;;
        -${noargopts}T)
            _comp_compgen -- -W 'aodv carp cnfp lmp pgm pgm_zmtp1 radius resp
                rpc rtcp rtp rtcp snmp tftp vat vxlan wb zmtp1'
            return
            ;;
        -${noargopts}z)
            _comp_compgen_commands
            return
            ;;
        --relinquish-privileges | -${noargopts}Z)
            _comp_compgen_allowed_users
            return
            ;;
        -${noargopts}[BcCDEGMsWy])
            return
            ;;
        --time-stamp-type | -${noargopts}j)
            _comp_compgen -- -W 'host host_lowprec host_hiprec adapter
                adapter_unsynced'
            return
            ;;
        --direction | -${noargopts}Q)
            _comp_compgen -- -W 'in out inout'
            return
            ;;
        --time-stamp-precision)
            _comp_compgen -- -W 'micro nano'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi

} &&
    complete -F _comp_cmd_tcpdump tcpdump

# ex: filetype=sh
