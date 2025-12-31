# getconf(1) completion                                    -*- shell-script -*-

_comp_cmd_getconf()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -a)
            _comp_compgen_filedir
            return
            ;;
        -v)
            _comp_compgen -c "${cur:-POSIX_V}" split -- "$(
                "$1" -a 2>/dev/null | _comp_awk '{ print $1 }'
            )"
            return
            ;;
    esac

    if [[ $prev == PATH_MAX ]]; then # TODO more path vars, better handling
        _comp_compgen_filedir
    elif [[ $cur == -* ]]; then
        _comp_compgen -- -W '-a -v'
    else
        _comp_compgen_split -- "$(
            "$1" -a 2>/dev/null | _comp_awk '{ print $1 }'
        )"
    fi
} &&
    complete -F _comp_cmd_getconf getconf

# ex: filetype=sh
