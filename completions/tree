# tree(1) completion                                       -*- shell-script -*-

_comp_cmd_tree()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[LPIHTo]*)'
    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}[LPIHT] | --filelimit | --timefmt | --help | --version)
            return
            ;;
        --charset)
            _comp_compgen -x iconv charsets
            return
            ;;
        -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
        --sort)
            _comp_compgen -- -W "name version size mtime ctime"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    # Note: bash-4.2 has a bug with [[ ${arr[*]} == *text* ]], so we
    # assign ${words[*]} in a temporary variable "line".
    local line="${words[*]}"
    if [[ $line == *\ --fromfile\ * ]]; then
        _comp_compgen_filedir
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_tree tree

# ex: filetype=sh
