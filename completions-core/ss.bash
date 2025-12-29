# ss(8) completion                                         -*- shell-script -*-

_comp_cmd_ss()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[fADF]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV])
            return
            ;;
        --family | -${noargopts}f)
            _comp_compgen -- -W 'unix inet inet6 link netlink'
            return
            ;;
        --query | -${noargopts}A)
            local queries=$("$1" --help |
                command sed -e 's/|/ /g' -ne 's/.*QUERY := {\([^}]*\)}.*/\1/p')
            _comp_delimited , -W '$queries'
            return
            ;;
        --diag | --filter | -${noargopts}[DF])
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    elif [[ $prev == state ]]; then
        _comp_compgen -- -W 'all connected synchronized bucket big established
            syn-sent syn-recv fin-wait-{1,2} time-wait closed close-wait
            last-ack listening closing'
    fi
} &&
    complete -F _comp_cmd_ss ss

# ex: filetype=sh
