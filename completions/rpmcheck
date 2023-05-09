# bash completion for rpmcheck                             -*- shell-script -*-

_comp_cmd_rpmcheck()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -base)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-explain -failures -successes -dump -dump-all
            -base -help -compressed-input'
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_rpmcheck rpmcheck

# ex: filetype=sh
