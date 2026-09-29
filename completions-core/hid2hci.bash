# hid2hci completion

_comp_cmd_hid2hci()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--help --quiet -0 --tohci -1 --tohid'
    fi
} &&
    complete -F _comp_cmd_hid2hci hid2hci
