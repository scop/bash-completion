# mailmanctl completion                                    -*- shell-script -*-

_comp_cmd_mailmanctl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--no-restart --run-as-user --stale-lock-cleanup
            --quiet --help'
    else
        _comp_compgen -- -W 'start stop restart reopen'
    fi

} &&
    complete -F _comp_cmd_mailmanctl mailmanctl

# ex: filetype=sh
