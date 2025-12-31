# bash bind completion                                     -*- shell-script -*-

_comp_cmd_bind()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[lpPsSvVrxX])
            return
            ;;
        -*m)
            _comp_compgen -- -W "emacs emacs-standard emacs-meta emacs-ctlx vi
                vi-move vi-command vi-insert"
            return
            ;;
        -*f)
            _comp_compgen_filedir
            return
            ;;
        -*[qu])
            _comp_compgen_split -- "$("$1" -l)"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -c help -s "$1"
        return
    fi

    _comp_compgen -- -A binding
} &&
    complete -F _comp_cmd_bind bind

# ex: filetype=sh
