# dict(1) completion                                       -*- shell-script -*-

_comp_cmd_dict__compgen_dictdata()
{
    # shellcheck disable=SC2086
    _comp_compgen_split -- "$(
        "$@" 2>/dev/null | command sed -ne \
            's/^[[:blank:]]\{1,\}\([^[:blank:]]*\).*$/\1/p'
    )"
}

_comp_cmd_dict()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local -a dict_command=("$1")
    local host="" port="" db i

    local noargopts='!(-*|*[hpdis]*)'
    for ((i = 1; i < cword; i++)); do
        # shellcheck disable=SC2254
        case ${words[i]} in
            --host | -${noargopts}h)
                host=${words[++i]}
                [[ $host ]] && dict_command+=(-h "$host")
                ;;
            --port | -${noargopts}p)
                port=${words[++i]}
                [[ $port ]] && dict_command+=(-p "$port")
                ;;
            --database | -${noargopts}d)
                db=${words[++i]}
                [[ $db ]] && dict_command+=(-d "$db")
                ;;
        esac
    done

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    # shellcheck disable=SC2254
    case $prev in
        --database | -info | -${noargopts}[di])
            _comp_cmd_dict__compgen_dictdata "${dict_command[@]}" -D
            return
            ;;
        --strategy | -${noargopts}s)
            _comp_cmd_dict__compgen_dictdata "${dict_command[@]}" -S
            return
            ;;
    esac

    local dictfile=/usr/share/dict/words
    if [[ -r $dictfile ]]; then
        # Dictfile may be too large for practical compgen -W usage, so narrow
        # it down with grep if $cur looks like something that's safe to embed
        # in a pattern instead.
        if [[ $cur == +([-A-Za-z0-9/.]) ]]; then
            _comp_compgen_split -- "$(
                command grep "^${cur//./\\.}" "$dictfile"
            )"
        else
            _comp_compgen_split -- "$(cat "$dictfile")"
        fi
    fi
} &&
    complete -F _comp_cmd_dict -o default dict rdict

# ex: filetype=sh
