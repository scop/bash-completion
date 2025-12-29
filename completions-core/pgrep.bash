# pgrep(1) and pkill(1) completion                         -*- shell-script -*-

_comp_cmd_pgrep()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[cdgJMNstTzFGPuU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --delimiter | --pgroup | --session | --terminal | -${noargopts}[cdgJMNstTz])
            return
            ;;
        --signal)
            _comp_compgen_signals
            return
            ;;
        --pidfile | -${noargopts}F)
            _comp_compgen_filedir
            return
            ;;
        --group | -${noargopts}G)
            _comp_compgen_gids
            return
            ;;
        -j)
            _comp_compgen -- -W 'any none'
            return
            ;;
        --parent | --ns | -${noargopts}P)
            _comp_compgen_pids
            return
            ;;
        --euid | --uid | -${noargopts}[uU])
            _comp_compgen_uids
            return
            ;;
        --nslist)
            _comp_compgen -c "${cur##*,}" split -F $' \t\n,' -- "$(
                "$1" --help 2>&1 |
                    command sed -ne 's/^[[:space:]]*Available namespaces://p'
            )" &&
                _comp_delimited , -W '"${COMPREPLY[@]}"'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help ||
            _comp_compgen_usage - <<<"$("$1" --usage 2>&1 |
                command sed -e "s/\[-signal\]//" -e "s/\[-SIGNAL\]//")"
        [[ $cword -eq 1 && $1 == *pkill ]] && _comp_compgen -a signals -
        return
    fi

    _comp_compgen_pnames -s
} &&
    complete -F _comp_cmd_pgrep pgrep pkill

# ex: filetype=sh
