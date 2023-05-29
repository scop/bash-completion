# bash completion for iptables                             -*- shell-script -*-

_comp_cmd_iptables()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local table="" chain='s/^Chain \([^ ]\{1,\}\).*$/\1/p'
    local targets='ACCEPT DROP LOG ULOG REJECT'

    local IFS=$' \t\n' # for ${table:+-t "$table"}
    [[ ${words[*]} =~ [[:space:]]-(t|-table=?)[[:space:]]*([^[:space:]]+) ]] &&
        table=${BASH_REMATCH[2]}

    case $prev in
        -*[AIDRPFXLZ])
            _comp_compgen_split -- "$(
                "$1" ${table:+-t "$table"} -nL 2>/dev/null |
                    command sed -ne 's/^Chain \([^ ]\{1,\}\).*$/\1/p'
            )"
            ;;
        -*t)
            _comp_compgen -- -W 'nat filter mangle'
            ;;
        -j)
            if [[ $table == "filter" || ! $table ]]; then
                _comp_compgen -- -W '$targets'
                _comp_compgen -a split -- "$("$1" ${table:+-t "$table"} -nL \
                    2>/dev/null | command sed -ne "$chain" \
                    -e 's/INPUT|OUTPUT|FORWARD|PREROUTING|POSTROUTING//')"
            elif [[ $table == "nat" ]]; then
                _comp_compgen -- -W '$targets MIRROR SNAT DNAT MASQUERADE'
                _comp_compgen -a split -- "$("$1" -t "$table" -nL 2>/dev/null |
                    command sed -ne "$chain" \
                        -e 's/OUTPUT|PREROUTING|POSTROUTING//')"
            elif [[ $table == "mangle" ]]; then
                _comp_compgen -- -W '$targets MARK TOS'
                _comp_compgen -a split -- "$("$1" -t "$table" -nL 2>/dev/null |
                    command sed -ne "$chain" \
                        -e 's/INPUT|OUTPUT|FORWARD|PREROUTING|POSTROUTING//')"
            fi
            ;;
        *)
            if [[ $cur == -* ]]; then
                _comp_compgen_help - <<<"$("$1" --help 2>&1 |
                    command sed -e "s/^\[\!\]//")"
                [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            fi
            ;;
    esac

} &&
    complete -F _comp_cmd_iptables iptables

# ex: filetype=sh
