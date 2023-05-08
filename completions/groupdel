# groupdel(8) completion                                   -*- shell-script -*-

_comp_cmd_groupdel()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help)
            return
            ;;
        -R | --root)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -g
} &&
    complete -F _comp_cmd_groupdel groupdel

# ex: filetype=sh
