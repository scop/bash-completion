# bash completion for checksec                             -*- shell-script -*-

_comp_cmd_checksec()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --version | --help)
            return
            ;;
        --file | --fortify-file)
            _comp_compgen_filedir
            return
            ;;
        --dir)
            _comp_compgen_filedir -d
            return
            ;;
        --proc)
            _comp_compgen_pnames
            return
            ;;
        --proc-libs | --fortify-proc)
            _comp_compgen_pids
            return
            ;;
        --format)
            _comp_compgen_split -- "$("$1" --help 2>/dev/null |
                command sed -ne 's/[{,}]/ /g;s/^[[:space:]]*--format=//p')"
            ;;
        --output)
            _comp_compgen_split -- "$("$1" --help 2>/dev/null |
                command sed -ne 's/[{,}]/ /g;s/^[[:space:]]*--output=//p')"
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_checksec checksec

# ex: filetype=sh
