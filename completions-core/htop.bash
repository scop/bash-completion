# htop(1) completion                                       -*- shell-script -*-

_comp_cmd_htop()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[sud]*)'
    # shellcheck disable=SC2254
    case "$prev" in
        --sort-key | -${noargopts}s)
            _comp_compgen_split -- "$("$1" -s help)"
            return
            ;;
        --user | -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
        --delay | -${noargopts}d)
            # argument required but no completions available
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_htop htop

# ex: filetype=sh
