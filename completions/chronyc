# chronyc(1) completion                                    -*- shell-script -*-

_comp_cmd_chronyc__command_args()
{
    local -a args
    _comp_split args "$("$1" help 2>/dev/null |
        _comp_awk '/^'"$prev"'[ \t][^ []/ { gsub("\\|", " ", $2); print $2 }')"
    case $args in
        \<address\>) _comp_compgen_known_hosts -- "$cur" ;;
        \<*) ;;
        *) ((${#args[@]})) &&
            _comp_compgen -a -- -W '"${args[@]}"' ;;
    esac
}

_comp_cmd_chronyc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | -*p)
            return
            ;;
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        _comp_compgen -a -- -W '-6'
        return
    fi

    local i args
    args=0
    for ((i = 1; i < cword; i++)); do
        [[ ${words[i]} != -* && ${words[i - 1]} != @(-p|-h) ]] && ((args++))
    done

    case $args in
        0)
            _comp_compgen_split -- "$("$1" help 2>/dev/null |
                _comp_awk '!/(^ |: *$)/ { sub("\\|", " ", $1); print $1 }')"
            ;;
        1)
            _comp_cmd_chronyc__command_args "$1"
            if [[ ! ${COMPREPLY-} && $prev == sources?(tats) ]]; then
                # [-v] not handled by _comp_cmd_chronyc__command_args yet
                _comp_compgen -- -W '-v'
            fi
            ;;
        2)
            [[ $prev == @(peer|server) ]] && _comp_compgen_known_hosts -- "$cur"
            ;;
    esac
} &&
    complete -F _comp_cmd_chronyc chronyc

# ex: filetype=sh
