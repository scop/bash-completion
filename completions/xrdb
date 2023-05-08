# xrdb(1) completion                                       -*- shell-script -*-

_comp_cmd_xrdb()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -backup | -display | -help)
            return
            ;;
        -cpp | -edit)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_xrdb xrdb

# ex: filetype=sh
