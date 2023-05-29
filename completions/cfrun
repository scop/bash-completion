# cfrun completion                                         -*- shell-script -*-

_comp_cmd_cfrun()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local i section=1
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == -- ]]; then
            ((section++))
        fi
    done

    case $section in
        1)
            case $prev in
                -f)
                    _comp_compgen_filedir
                    return
                    ;;
            esac

            if [[ $cur == -* ]]; then
                _comp_compgen -- -W '-f -h -d -S -T -v'
            else
                local hostfile=${CFINPUTS:-/var/lib/cfengine/inputs}/cfrun.hosts
                for ((i = 1; i < cword; i++)); do
                    if [[ ${words[i]} == -f ]]; then
                        hostfile=${words[i + 1]}
                        break
                    fi
                done
                [[ ! -f $hostfile ]] && return

                _comp_compgen_split -- "$(command grep -v -E '(=|^$|^#)' \
                    "$hostfile")"
            fi
            ;;
        2)
            _comp_compgen_help -c cfagent --help
            ;;
    esac
} &&
    complete -F _comp_cmd_cfrun cfrun

# ex: filetype=sh
