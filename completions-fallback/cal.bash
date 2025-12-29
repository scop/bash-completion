# cal(1) completion                                        -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_cal()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -m)
            if [[ $OSTYPE == *bsd* ]]; then
                _comp_compgen -- -W '{1..12}'
                return
            fi
            ;;
        -s)
            [[ $OSTYPE == *bsd* ]] && return
            ;;
        -A | -B | -d | -H)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    local REPLY
    _comp_count_args
    ((REPLY == 1)) && _comp_compgen -- -W '{1..12}'
} &&
    complete -F _comp_cmd_cal cal ncal

# ex: filetype=sh
