# ssh-add(1) completion                                    -*- shell-script -*-

_comp_cmd_ssh_add()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*E)
            _comp_compgen -- -W 'md5 sha256'
            return
            ;;
        -*H)
            _comp_compgen_filedir
            return
            ;;
        -*h)
            # TODO should we try supporting more types of constraints?
            if [[ $cur == *@* ]]; then
                _comp_complete_user_at_host "$@"
            else
                _comp_compgen_known_hosts -- "$cur"
            fi
            return
            ;;
        -*t)
            return
            ;;
        -*T)
            _comp_compgen_filedir
            return
            ;;
        -*S | -*[se])
            _comp_compgen_filedir so
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- '-?' || _comp_compgen_help -- '-?'
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_ssh_add ssh-add

# ex: filetype=sh
