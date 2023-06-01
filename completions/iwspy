# iwspy completion                                         -*- shell-script -*-

_comp_cmd_iwspy()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--help --version'
        else
            _comp_compgen_available_interfaces -w
        fi
    else
        _comp_compgen -- -W 'setthr getthr off'
    fi
} &&
    complete -F _comp_cmd_iwspy iwspy

# ex: filetype=sh
