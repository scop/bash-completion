# bash completion for ebtables                             -*- shell-script -*-

_comp_cmd_ebtables()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local table="" chain='s/^Bridge chain: \([^ ,]\{1,\}\).*$/\1/p' \
        targets='ACCEPT DROP CONTINUE RETURN'

    local IFS=$' \t\n' # for ${table:+-t "$table"}
    [[ ${words[*]} =~ [[:space:]]-(t|-table=?)[[:space:]]*([^[:space:]]+) ]] &&
        table=${BASH_REMATCH[2]}

    local noargopts='!(-*|*[AIDPFXLZtj]*)'
    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}[AIDPFXLZ])
            _comp_compgen_split -- "$(
                "$1" ${table:+-t "$table"} -L 2>/dev/null |
                    command sed -ne "$chain"
            )"
            ;;
        -${noargopts}t)
            _comp_compgen -- -W 'nat filter broute'
            ;;
        -${noargopts}j)
            if [[ $table == "filter" || ! $table ]]; then
                _comp_compgen -- -W '$targets'
                _comp_compgen -a split -- "$("$1" ${table:+-t "$table"} -L \
                    2>/dev/null | command sed -n -e \
                    "s/INPUT\|OUTPUT\|FORWARD//" -e "$chain")"
            elif [[ $table == "nat" ]]; then
                _comp_compgen -- -W '$targets'
                _comp_compgen -a split -- "$("$1" -t "$table" -L 2>/dev/null |
                    command sed -n -e "s/OUTPUT|PREROUTING|POSTROUTING//" \
                        -e "$chain")"
            elif [[ $table == "broute" ]]; then
                _comp_compgen -- -W 'ACCEPT DROP'
                _comp_compgen -a split -- "$("$1" -t "$table" -L 2>/dev/null |
                    command sed -n -e "s/BROUTING//" -e "$chain")"
            fi
            ;;
        *)
            if [[ $cur == -* ]]; then
                _comp_compgen -- -W '--802_3-sap --802_3-type --among-dst
            --among-dst-file --among-src --among-src-file --append
            --arp-gratuitous --arp-htype --arp-ip-dst --arp-ip-src
            --arp-mac-dst --arp-mac-src --arp-opcode --arp-ptype --arpreply-mac
            --arpreply-target --atomic-commit --atomic-file --atomic-init
            --atomic-save --change-counters --concurrent --delete
            --delete-chain --destination --dnat-target --dst --flush --help
            --in-if --in-interface --init-table --insert --ip6-destination
            --ip6-destination-port --ip6-dport --ip6-dst --ip6-icmp-type
            --ip6-prococol --ip6-proto --ip6-protocol --ip6-source
            --ip6-source-port --ip6-sport --ip6-src --ip6-tclass
            --ip-destination --ip-destination-port --ip-dport --ip-dst
            --ip-proto --ip-protocol --ip-source --ip-source-port --ip-sport
            --ip-src --ip-tos --jump --Lc --limit --limit-burst --list --Lmac2
            --Ln --log --log-arp --logical-in --logical-out --log-ip --log-ip6
            --log-level --log-prefix --Lx --mark --mark-and --mark-or
            --mark-set --mark-target --mark-xor --modprobe --new-chain --nflog
            --nflog-group --nflog-prefix --nflog-range --nflog-threshold
            --out-if --out-interface --pkttype-type --policy --proto --protocol
            --redirect-target --rename-chain --set-counter --snat-arp
            --snat-target --source --src --stp-flags --stp-forward-delay
            --stp-hello-time --stp-max-age --stp-msg-age --stp-port
            --stp-root-addr --stp-root-cost --stp-root-prio --stp-sender-addr
            --stp-sender-prio --stp-type --table --to-destination --to-dst
            --to-source --to-src --ulog --ulog-cprange --ulog-nlgroup
            --ulog-prefix --ulog-qthreshold --version --vlan-encap --vlan-id
            --vlan-prio --zero'
            fi
            ;;
    esac

} &&
    complete -F _comp_cmd_ebtables ebtables

# ex: filetype=sh
