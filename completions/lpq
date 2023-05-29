# lpq(1) completion                                        -*- shell-script -*-

_comp_cmd_lpq()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -P)
            _comp_compgen_split -- "$(lpstat -a 2>/dev/null | cut -d' ' -f1)"
            return
            ;;
        -U)
            _comp_compgen -- -u
            return
            ;;
    esac

    if [[ $cur == - ]]; then
        _comp_compgen -- -W '-E -P -U -a -h -l'
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_lpq lpq

# ex: filetype=sh
