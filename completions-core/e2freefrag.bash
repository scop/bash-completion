# e2freefrag(8) completion                                 -*- shell-script -*-

_comp_cmd_e2freefrag()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c | -h)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- -h
        return
    fi

    _comp_compgen -c "${cur:-/dev/}" filedir
} &&
    complete -F _comp_cmd_e2freefrag e2freefrag

# ex: filetype=sh
