# e2label(8) completion

_comp_cmd_e2label()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -c "${cur:-/dev/}" filedir
    fi
} &&
    complete -F _comp_cmd_e2label e2label
