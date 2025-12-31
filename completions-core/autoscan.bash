# autoscan(1) completion                                   -*- shell-script -*-

_comp_cmd_autoscan()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[BI]*)'
    # shellcheck disable=SC2254
    case "$prev" in
        --help | --version | -${noargopts}[hV])
            return
            ;;
        --prepend-include | --include | -${noargopts}[BI])
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    if [[ $1 == *autoupdate ]]; then
        _comp_compgen_filedir '@(ac|in)'
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_autoscan autoscan autoupdate

# ex: filetype=sh
