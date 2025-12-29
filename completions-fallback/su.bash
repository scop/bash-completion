# bash completion for su(1)                                -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

if [[ $OSTYPE != *linux* ]]; then
    complete -u su # default completion
    return
fi

_comp_cmd_su()
{ # linux-specific completion
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case "$prev" in
        -s | --shell)
            _comp_compgen_shells
            return
            ;;
        -c | --command | --session-command)
            _comp_compgen_commands
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen -- -u
} &&
    complete -F _comp_cmd_su su

# ex: filetype=sh
