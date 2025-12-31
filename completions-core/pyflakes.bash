# pyflakes(1) completion                                   -*- shell-script -*-

_comp_cmd_pyflakes()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | --version)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir py
} &&
    complete -F _comp_cmd_pyflakes pyflakes

# ex: filetype=sh
