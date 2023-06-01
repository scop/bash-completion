# iwpriv completion                                        -*- shell-script -*-

_comp_cmd_iwpriv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        roam)
            _comp_compgen -- -W 'on off'
            return
            ;;
        port)
            _comp_compgen -- -W 'ad-hoc managed'
            return
            ;;
    esac

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--help --version'
        else
            _comp_compgen_available_interfaces -w
        fi
    else
        _comp_compgen -- -W '--all roam port'
    fi
} &&
    complete -F _comp_cmd_iwpriv iwpriv

# ex: filetype=sh
