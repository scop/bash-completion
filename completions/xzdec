# xzdec(1) completion                                      -*- shell-script -*-

_comp_cmd_xzdec()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*M*)'
    # shellcheck disable=SC2254
    case $prev in
        --memory | -${noargopts}M)
            return
            ;;
        --help | --version | -${noargopts}[hV])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir xz # no lzma support here as of xz 4.999.9beta
} &&
    complete -F _comp_cmd_xzdec xzdec

# ex: filetype=sh
