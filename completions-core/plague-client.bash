# bash completion for plague-client                        -*- shell-script -*-

_comp_cmd_plague_client()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    ((cword == 1)) &&
        _comp_compgen -- -W 'build detail finish help is_paused kill list
            list_builders pause requeue unpause update_builders'
} &&
    complete -F _comp_cmd_plague_client plague-client

# ex: filetype=sh
