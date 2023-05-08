# luserdel(1) completion                                   -*- shell-script -*-

_comp_cmd_luserdel()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --usage | -!(-*)[?]*)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -u
} &&
    complete -F _comp_cmd_luserdel luserdel

# ex: filetype=sh
