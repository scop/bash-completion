# mailman sync_members completion                          -*- shell-script -*-

_comp_cmd_sync_members()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -w | -g | -d | --welcome-msg | --goodbye-msg | --digest)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --file)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--no-change --welcome-msg --goodbye-msg --digest
            --notifyadmin --file --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_compgen -x list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_sync_members sync_members

# ex: filetype=sh
