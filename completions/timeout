# timeout(1) completion                                    -*- shell-script -*-

_comp_cmd_timeout()
{
    local cur prev words cword was_split comp_args i
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[ks]*)'
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            _comp_command_offset "$((i + 1))"
            return
        fi
        # shellcheck disable=SC2254
        [[ ${words[i]} == -@(-kill-after|-signal|${noargopts}[ks]) ]] && ((i++))
    done

    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --kill-after | -${noargopts}k)
            return
            ;;
        --signal | -${noargopts}s)
            _comp_compgen_signals
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_timeout timeout

# ex: filetype=sh
