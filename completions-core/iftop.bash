# iftop(8) completion                                      -*- shell-script -*-

_comp_cmd_iftop()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -f | -F | -G | -m | -s | -L)
            return
            ;;
        -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -c)
            _comp_compgen_filedir
            return
            ;;
        -o)
            _comp_compgen -- -W "2s 10s 40s source destination"
            return
            ;;
    esac

    _comp_compgen_help -- -h
} &&
    complete -F _comp_cmd_iftop iftop

# ex: filetype=sh
