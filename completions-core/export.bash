# bash export completion                                   -*- shell-script -*-

_comp_cmd_export()
{
    local cur prev words cword comp_args
    _comp_initialize -n := -- "$@" || return

    local i action=variable remove=""
    for ((i = 1; i < cword; i++)); do
        case ${words[i]} in
            -p)
                return
                ;;
            -*f*)
                action=function
                ;;&
            -*n*)
                remove=set
                ;;
            -*)
                continue
                ;;
        esac
        break
    done

    if [[ $cur == *=* ]]; then
        _comp_variable_assignments "$cur" && return
    fi

    case $cur in
        *=)
            local pname=${cur%=}
            local REPLY
            _comp_quote "${!pname-}"
            local pval=$REPLY
            # Complete previous value if it's not empty.
            if [[ $pval != \'\' ]]; then
                COMPREPLY=("$pval")
            else
                _comp_compgen -c "${cur#*=}" filedir
            fi
            ;;
        *=*)
            _comp_compgen -c "${cur#*=}" filedir
            ;;
        *)
            if [[ $cword -eq 1 && $cur == -* ]]; then
                _comp_compgen_usage -c help -s "$1"
                _comp_compgen -a -- -W '-p'
                return
            fi
            local suffix=""
            if [[ ! $remove && $action != function ]]; then
                suffix="="
                compopt -o nospace
            fi
            _comp_compgen -- -A $action -S "$suffix"
            ;;
    esac
} &&
    complete -F _comp_cmd_export export

# ex: filetype=sh
