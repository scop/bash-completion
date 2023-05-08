# bash completion for Portsnap                             -*- shell-script -*-

[[ $OSTYPE == *freebsd* ]] || return 1

_comp_cmd_portsnap()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -d | -p)
            _comp_compgen_filedir -d
            return
            ;;
        -l | -f)
            _comp_compgen_filedir
            return
            ;;
    esac

    _comp_compgen -- -W "fetch cron extract update"
} &&
    complete -F _comp_cmd_portsnap portsnap

# ex: filetype=sh
