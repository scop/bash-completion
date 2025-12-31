# bash completion for mc                                   -*- shell-script -*-

_comp_cmd_mc()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[evlPCD]*)'
    # shellcheck disable=SC2254
    case $prev in
        --edit | --view | --ftplog | --printwd | -${noargopts}[evlP])
            _comp_compgen_filedir
            return
            ;;
        --help | --help-* | --version | --colors | --debuglevel | -${noargopts}[hVCD])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_mc mc

# ex: filetype=sh
