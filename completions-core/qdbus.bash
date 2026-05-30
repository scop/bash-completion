# Qt qdbus, dcop completion

_comp_cmd_qdbus()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_split -- "$(
        command "${words[@]::cword}" 2>/dev/null | command sed 's/(.*)//'
    )"
} &&
    complete -F _comp_cmd_qdbus qdbus dcop
