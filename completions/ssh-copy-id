# ssh-copy-id(1) completion                                -*- shell-script -*-

_comp_cmd_ssh_copy_id()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # Prefer `ssh` from same dir for resolving options, etc
    local pathcmd
    pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH

    _comp_compgen -x ssh suboption_check && return

    case $prev in
        -i)
            _comp_compgen -x ssh identityfile pub
            return
            ;;
        -p | -t)
            return
            ;;
        -F)
            _comp_compgen_filedir
            return
            ;;
        -o)
            _comp_compgen -x ssh options
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_compgen_known_hosts -a -- "$cur"
    fi
} &&
    complete -F _comp_cmd_ssh_copy_id ssh-copy-id

# ex: filetype=sh
