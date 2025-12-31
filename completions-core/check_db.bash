# mailman check_db completion                              -*- shell-script -*-

_comp_cmd_check_db()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--all --verbose --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_compgen -x list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_check_db check_db

# ex: filetype=sh
