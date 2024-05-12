# bash completion for set                                 -*- shell-script -*-

_comp_cmd_set()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[o]*)'

    # shellcheck disable=SC2254
    case "$prev" in
        [+-]${noargopts}o)
            _comp_compgen -- -A setopt
            return
            ;;
    esac

    local i want_options=set
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == -?(-) ]]; then
            want_options=""
            break
        fi
    done

    if [[ $want_options && $cur == [+-]* ]]; then
        local has_plus=""
        if [[ $cur == +?([a-zA-Z]) ]]; then
            has_plus=set
            cur=${cur/#+/-}
        fi
        _comp_compgen_usage
        if [[ $has_plus ]]; then
            local i
            for i in "${!COMPREPLY[@]}"; do
                if [[ ${COMPREPLY[i]} == -- ]]; then
                    unset -v 'COMPREPLY[i]'
                else
                    COMPREPLY[i]=${COMPREPLY[i]/#-/+}
                fi
            done
        fi
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_set set

# ex: filetype=sh
