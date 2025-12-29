# bash completion for reptyr(1)                            -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# reptyr > 0.6.2, use that instead.

_comp_cmd_reptyr()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -l)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    [[ $prev != +([0-9]) ]] && _comp_compgen_pids
} &&
    complete -F _comp_cmd_reptyr reptyr

# ex: filetype=sh
