# ipcalc(1) completion                                     -*- shell-script -*-

_comp_cmd_ipcalc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version | --split | -[hs])
            return
            ;;
    esac

    # --split takes 3 args
    local i
    for i in {1..3}; do
        [[ ${words[cword - i]} == -@(-split|s) ]] && return
    done

    [[ $cur != -* ]] ||
        _comp_compgen_help
} &&
    complete -F _comp_cmd_ipcalc ipcalc

# ex: filetype=sh
