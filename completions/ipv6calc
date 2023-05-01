# ipv6calc completion                                      -*- shell-script -*-

_comp_cmd_ipv6calc()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[dIOA]*)'
    # shellcheck disable=SC2254
    case "$prev" in
        --debug | -${noargopts}d)
            return
            ;;
        --in | --out | --action | -${noargopts}[IOA])
            # With ipv6calc < 0.73.0, -m does nothing here, so use sed instead.
            _comp_compgen_split -- "$("$1" "$prev" -h 2>&1 |
                command sed -ne 's/^[[:space:]]\{1,\}\([^[:space:]:]\{1,\}\)[[:space:]]*:.*/\1/p')"
            return
            ;;
        --db-geoip | --db-ip2location-ipv4 | --db-ip2location-ipv6)
            _comp_compgen_filedir
            return
            ;;
        --printstart | --printend)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help - <<<"$("$1" -h 2>&1 |
            command sed -e "s/[][]//g")"
    fi

} &&
    complete -F _comp_cmd_ipv6calc ipv6calc

# ex: filetype=sh
