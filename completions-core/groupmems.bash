# groupmems(8) completion                                  -*- shell-script -*-

_comp_cmd_groupmems()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -a | --add | -d | --delete)
            _comp_compgen -- -u
            return
            ;;
        -g | --group)
            _comp_compgen -- -g
            return
            ;;
        -R | --root)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    _comp_compgen_help
} &&
    complete -F _comp_cmd_groupmems groupmems

# ex: filetype=sh
