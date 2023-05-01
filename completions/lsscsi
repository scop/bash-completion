# lsscsi(8) completion                                     -*- shell-script -*-

_comp_cmd_lsscsi()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[y]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV]*)
            return
            ;;
        --sysfsroot | -${noargopts}y)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_lsscsi lsscsi

# ex: filetype=sh
