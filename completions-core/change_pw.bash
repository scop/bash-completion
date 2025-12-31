# mailman change_pw completion                             -*- shell-script -*-

_comp_cmd_change_pw()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -l | --listname)
            # Prefer `list_lists` in the same dir as command
            local pathcmd
            pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
            _comp_compgen -x list_lists mailman_lists
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--all --domain --listname --password --quiet
            --help'
    fi

} &&
    complete -F _comp_cmd_change_pw change_pw

# ex: filetype=sh
