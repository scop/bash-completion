# luac(1) completion                                       -*- shell-script -*-

_comp_cmd_luac()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -v | -)
            return
            ;;
        -o)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir lua
} &&
    complete -F _comp_cmd_luac luac{,5{,.}{0..4}}

# ex: filetype=sh
