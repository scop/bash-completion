# lua(1) completion                                        -*- shell-script -*-

_comp_cmd_lua()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -e | -l | -v | -)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir 'l@(ua|?(ua)c)'
} &&
    complete -F _comp_cmd_lua lua{,5{,.}{0..4}}

# ex: filetype=sh
