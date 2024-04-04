# mailman list_admins completion                           -*- shell-script -*-

_comp_cmd_list_admins()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--all-vhost --all --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_compgen -x list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_list_admins list_admins

# ex: filetype=sh
