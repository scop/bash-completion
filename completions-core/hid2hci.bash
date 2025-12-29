# hid2hci completion                                       -*- shell-script -*-

_comp_cmd_hid2hci()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--help --quiet -0 --tohci -1 --tohid'
    fi
} &&
    complete -F _comp_cmd_hid2hci hid2hci

# ex: filetype=sh
