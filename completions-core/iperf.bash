# iperf(1) completion                                      -*- shell-script -*-

_comp_cmd_iperf()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    local noargopts='!(-*|*[ilpwMXbntLPTZCkOAfIoFBcxy]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --interval | --len | --port | --window | --mss | --bandwidth | \
            --num | --time | --listenport | --parallel | --ttl | --linux-congestion | --omit | \
            --congestion | --bytes | --blockcount | --cport | --set-mss | --flowlabel | \
            --title | --affinity | --rcv-timeout | --server-bitrate-limit | \
            --idle-timeout | --time-skew-threshold | --xbind | --nstreams | --connect-timeout | \
            --bitrate | --pacing-timer | --fq-rate | --length | --dscp | --extra-data | \
            --username | -${noargopts}[hvilpwMXbntLPTZCkOA])
            return
            ;;
        --format | -${noargopts}f)
            local formats=$(
                "$1" --help 2>&1 |
                    command sed -ne 's/^.*--format .*\[\([a-zA-Z]\{1,\}\)\].*/\1/p' |
                    command sed -e 's/./& /g'
            )
            _comp_compgen -- -W '$formats'
            return
            ;;
        --pidfile | -${noargopts}I)
            _comp_compgen_filedir pid
            return
            ;;
        --output | --fileinput | --authorized-users-path | -${noargopts}[oF])
            _comp_compgen_filedir
            return
            ;;
        --bind | -${noargopts}B)
            _comp_compgen_available_interfaces -a
            _comp_compgen -a ip_addresses -a
            return
            ;;
        --bind-dev)
            _comp_compgen_available_interfaces -a
            return
            ;;
        --client | -${noargopts}c)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --reportexclude | -${noargopts}x)
            _comp_compgen -- -W 'C D M S V'
            return
            ;;
        --reportstyle | -${noargopts}y)
            _comp_compgen -- -W 'C'
            return
            ;;
        --logfile)
            _comp_compgen_filedir log
            return
            ;;
        --tos | -${noargopts}S)
            _comp_compgen -- -W '{0..255}'
            return
            ;;
        --rsa-private-key-path | --rsa-public-key-path)
            _comp_compgen_filedir pem
            return
            ;;
    esac

    [[ $was_split ]] && return

    # Filter mode specific options
    local -a filter=(cat)
    local i
    for i in "${words[@]}"; do
        case $i in
            -s | --server)
                filter=(command sed -e '/^Client.specific/,/^\(Server.specific.*\)\{0,1\}$/d')
                ;;
            -c | --client)
                filter=(command sed -e '/^Server.specific/,/^\(Client.specific.*\)\{0,1\}$/d')
                ;;
        esac
    done
    [[ $filter != cat ]] && filter+=(-e '/--client/d' -e '/--server/d')

    _comp_compgen_help - <<<"$("$1" --help 2>&1 | "${filter[@]}")"
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_iperf iperf iperf3

# ex: filetype=sh
