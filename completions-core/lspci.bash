# lspci(8) completion                                      -*- shell-script -*-

_comp_cmd_lspci()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[sDO])
            return
            ;;
        -*i)
            _comp_compgen_filedir ids
            return
            ;;
        -*p)
            _comp_compgen_filedir pcimap
            return
            ;;
        -*A)
            _comp_compgen_split -- "$("$1" -A help | command grep -vF :)"
            return
            ;;
        -*H)
            _comp_compgen -- -W "1 2"
            return
            ;;
        -*F)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_lspci lspci

# ex: filetype=sh
