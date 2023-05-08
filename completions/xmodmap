# xmodmap(1) completion                                    -*- shell-script -*-

_comp_cmd_xmodmap()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -display | -e)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_xmodmap xmodmap

# ex: filetype=sh
