# ionice(1) completion                                     -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# util-linux >= 2.23, use that instead.

_comp_cmd_ionice()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local offset=0 i
    for ((i = 1; i <= cword; i++)); do
        case ${words[i]} in
            -h)
                return
                ;;
            -p)
                offset=0
                break
                ;;
            -c | -n)
                ((i++))
                continue
                ;;
            -*)
                continue
                ;;
        esac
        offset=$i
        break
    done

    if ((offset > 0)); then
        _comp_command_offset $offset
        return
    fi

    case $prev in
        -c)
            _comp_compgen -- -W '{0..3}'
            return
            ;;
        -n)
            _comp_compgen -- -W '{0..7}'
            return
            ;;
        -p)
            _comp_compgen_pids
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi
} &&
    complete -F _comp_cmd_ionice ionice

# ex: filetype=sh
