# avctrl completion                                        -*- shell-script -*-

_comp_cmd_avctrl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--help --quiet'
    else
        local REPLY
        _comp_count_args
        if ((REPLY == 1)); then
            _comp_compgen -- -W 'discover switch'
        fi
    fi
} &&
    complete -F _comp_cmd_avctrl avctrl

# ex: filetype=sh
