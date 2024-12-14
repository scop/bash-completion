# doas(1) completion                                       -*- shell-script -*-

_comp_cmd_doas()
{
    local cur prev words cword split
    _init_completion -s || return

    local i

    for ((i = 1; i <= cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            local PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin
            local root_command=${words[i]}
            _command_offset $i
            return
        fi
        [[ ${words[i]} == -@(!(-*)[uCLs]) ]] &&
            ((i++))
    done

    case "$prev" in
        -!(-*)u)
            COMPREPLY=($(compgen -u -- "$cur"))
            return
            ;;
        -!(-*)C)
            _filedir
            return
            ;;
        -!(-*)[Ls])
            return
            ;;
    esac

    $split && return

    if [[ $cur == -* ]]; then
        COMPREPLY=($(compgen -W '$(_parse_usage "$1")' -- "$cur"))
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_doas doas

# ex: filetype=sh
