# ssh-copy-id(1) completion

_comp_cmd_ssh_copy_id()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # Prefer `ssh` from same dir for resolving options, etc
    local pathcmd cmdprefix
    pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
    cmdprefix=${1##*/}
    cmdprefix=${cmdprefix%ssh-copy-id}

    _comp_compgen -x ssh suboption_check "${cmdprefix}ssh" && return

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
            _comp_compgen -x ssh options "${cmdprefix}ssh"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_compgen_known_hosts -a
    fi
} &&
    complete -F _comp_cmd_ssh_copy_id {hpn,}ssh-copy-id
