# mailman list_owners completion                           -*- shell-script -*-

_comp_cmd_list_owners()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--with-listnames --moderators --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_compgen -x list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_list_owners list_owners

# ex: filetype=sh
