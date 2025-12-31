# chkconfig(8) completion                                  -*- shell-script -*-

_comp_cmd_chkconfig()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --level=[1-6] | [1-6] | --list | --add | --del | --override)
            _comp_compgen_services
            _comp_compgen -a xinetd_services
            return
            ;;
        --level)
            _comp_compgen -- -W '{1..6}'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--list --add --del --override --level'
    else
        if ((cword == 2 || cword == 4)); then
            _comp_compgen -- -W 'on off reset resetpriorities'
        else
            _comp_compgen_services
            _comp_compgen -a xinetd_services
        fi
    fi
} &&
    complete -F _comp_cmd_chkconfig chkconfig

# ex: filetype=sh
