# bash shell function completion                           -*- shell-script -*-

_comp_cmd_function()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -A function
    else
        local funcdef=$(type -- "${words[1]}" 2>/dev/null | _comp_tail -n +3)
        COMPREPLY=("()${funcdef:+ $funcdef}")
    fi
} &&
    complete -F _comp_cmd_function function

# ex: filetype=sh
