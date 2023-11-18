# iconv(1) completion                                      -*- shell-script -*-

# @since 2.12
_comp_xfunc_iconv_compgen_charsets()
{
    _comp_cmd_iconv__compgen_charsets iconv
}

# @deprecated 2.12 use `_comp_xfunc_iconv_compgen_charsets` instead
_iconv_charsets()
{
    _comp_compgen -ai iconv charsets "${1:-iconv}"
}

_comp_cmd_iconv__compgen_charsets()
{
    _comp_compgen_split -X ... -- "$("$1" -l |
        command sed -e 's@/*$@@' -e 's/[,()]//g')"
}

_comp_cmd_iconv()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[fto]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --usage | --version | --unicode-subst | --byte-subst | \
            --widechar-subst | -${noargopts}[?V])
            return
            ;;
        --from-code | --to-code | -${noargopts}[ft])
            _comp_cmd_iconv__compgen_charsets "$1"
            return
            ;;
        --output | -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_iconv -o default iconv

# ex: filetype=sh
