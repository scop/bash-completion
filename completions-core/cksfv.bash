# cksfv completion by Chris <xris@forevermore.net>         -*- shell-script -*-

_comp_cmd_cksfv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen_help
        return
    fi

    case "$prev" in
        -*C | -*g)
            _comp_compgen_filedir -d
            return
            ;;
        -*f)
            _comp_compgen_filedir 'sfv'
            return
            ;;
    esac

    _comp_compgen_filedir

} &&
    complete -F _comp_cmd_cksfv cksfv

# ex: filetype=sh
