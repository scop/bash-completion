# doas(1) completion

_comp_cmd_doas()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[uCLs]*)'

    local i
    for ((i = 1; i <= cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            local PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin
            local root_command=${words[i]}
            local _comp_root_command=1
            _comp_command_offset "$i"
            return
        fi
        [[ ${words[i]} == -@(${noargopts}[uCLs]) ]] &&
            ((i++))
    done

    # shellcheck disable=SC2254 # glob $noargopts should not be quoted
    case $prev in
        -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
        -${noargopts}C)
            _comp_compgen_filedir
            return
            ;;
        -${noargopts}[Ls])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_doas doas
