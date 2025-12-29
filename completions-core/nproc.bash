# nproc(1) completion                                      -*- shell-script -*-

_comp_cmd_nproc()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --help | --version | --ignore)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_nproc nproc

# ex: filetype=sh
