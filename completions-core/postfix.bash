# postfix(1) completion                                    -*- shell-script -*-

_comp_cmd_postfix()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            _comp_compgen_filedir -d
            return
            ;;
        -D)
            _comp_compgen -- -W 'start'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -c _comp_try_faketty "$1" --help
        return
    fi

    _comp_compgen -- -W 'check start stop abort flush reload status
        set-permissions upgrade-configuration'
} &&
    complete -F _comp_cmd_postfix postfix

# ex: filetype=sh
