# iwlist completion                                        -*- shell-script -*-

_comp_cmd_iwlist()
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
        _comp_compgen -- -W 'scan scanning freq frequency channel rate bit
            bitrate key enc encryption power txpower retry ap accesspoint peers
            event'
    fi
} &&
    complete -F _comp_cmd_iwlist iwlist

# ex: filetype=sh
