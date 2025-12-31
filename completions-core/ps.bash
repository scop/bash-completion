# bash completion for ps(1)                                -*- shell-script -*-

_comp_cmd_ps()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help)
            _comp_compgen -- -W 'simple list output threads misc all'
            return
            ;;
        --info | V | --version)
            return
            ;;
        -C)
            _comp_compgen_pnames
            return
            ;;
        -[Gg] | --[Gg]roup)
            _comp_compgen -- -g
            return
            ;;
        ?(-)p | [^-]*p | --pid)
            _comp_compgen_pids
            return
            ;;
        --ppid)
            _comp_compgen_pids # TODO: Only pids with children?
            return
            ;;
        ?(-)q | [^-]*q | --quick-pid)
            _comp_compgen_pids
            return
            ;;
        -s | --sid)
            # TODO
            return
            ;;
        ?(-)t | [^-]*t | --tty)
            _comp_expand_glob COMPREPLY '/dev/tty*' &&
                _comp_compgen -- -W '"${COMPREPLY[@]}" "${COMPREPLY[@]#/dev/}"'
            return
            ;;
        ?(-)U | [^-]*U | -u | --[Uu]ser)
            _comp_compgen -- -u
            return
            ;;
        --format | ?(-)[Oo] | [^-]*[Oo])
            # TODO: This doesn't work well when there are multiple options for
            # the non-first item (similarly to useradd --groups and others).
            local labels=$("$1" L | _comp_awk '{ print $1 }')
            _comp_delimited , -W '$labels'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        # sed: strip single char dashless ", x," that trip _comp_compgen_help
        _comp_compgen_help - <<<"$({
            "$1" --help
            "$1" --help all
        } 2>/dev/null |
            command sed -e "s/, [A-Za-z],/,/")" ||
            _comp_compgen_usage
    fi
} &&
    complete -F _comp_cmd_ps ps

# ex: filetype=sh
