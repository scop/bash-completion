# bash completion for deja-dup(1)                          -*- shell-script -*-

_comp_cmd_deja_dup()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -'?' | --help | --help-*)
            return
            ;;
        --restore)
            _comp_compgen_filedir
            return
            ;;
        --restore-missing)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_deja_dup deja-dup

# ex: filetype=sh
