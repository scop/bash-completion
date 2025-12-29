# bash completion for free(1)                              -*- shell-script -*-

_comp_cmd_free()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[cs]*)'
    case $prev in
        --help | --version | --count | --seconds | -${noargopts}[hVcs])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
    fi
} &&
    complete -F _comp_cmd_free free

# ex: filetype=sh
