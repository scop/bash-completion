# mailman add_members completion                           -*- shell-script -*-

_comp_cmd_add_members()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -r | -d | --regular-members-file | --digest-members-file)
            _comp_compgen_filedir
            return
            ;;
        -w | -a | --welcome-msg | --admin-notify)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--regular-members-file --digest-members-file
            --welcome-msg --admin-notify --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_xfunc list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_add_members add_members

# ex: filetype=sh
