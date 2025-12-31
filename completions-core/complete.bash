# bash complete completion                                 -*- shell-script -*-

_comp_cmd_complete()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*o)
            _comp_compgen -- -W 'bashdefault default dirnames filenames nospace
                plusdirs'
            return
            ;;

        -*A)
            _comp_compgen -- -W 'alias arrayvar binding builtin command
                directory disabled enabled export file function group helptopic
                hostname job keyword running service setopt shopt signal
                stopped user variable'
            return
            ;;

        -*C)
            _comp_compgen -- -A command
            return
            ;;
        -*F)
            _comp_compgen -- -A function
            return
            ;;
        -*p | -*r)
            _comp_compgen_split -l -- "$(complete -p | command sed -e 's|.* ||')"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        local -a opts
        _comp_compgen -v opts usage -c help -s "$1"
        # -F, -C do not work the expected way with compgen
        [[ $1 != *compgen ]] || opts=("${opts[@]//-[FC]/}")
        _comp_compgen -- -W '"${opts[@]}"' -X ''
    else
        _comp_compgen -- -A command
    fi
} &&
    complete -F _comp_cmd_complete compgen complete

# ex: filetype=sh
