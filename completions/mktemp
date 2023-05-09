# mktemp(1) completion                                     -*- shell-script -*-

_comp_cmd_mktemp()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[p]*)'
    # shellcheck disable=SC2254
    case "$prev" in
        --help | --version | --suffix)
            return
            ;;
        --tmpdir | -${noargopts}p)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help ||
            _comp_compgen -- -W '-d -u -q -p -t' # non-GNU fallback
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_mktemp mktemp

# ex: filetype=sh
