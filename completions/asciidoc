# asciidoc(1) completion                                   -*- shell-script -*-

# @since 2.12
_comp_xfunc_asciidoc_compgen_doctype()
{
    _comp_compgen -- -W 'article book manpage'
}

# @deprecated 2.12
_asciidoc_doctype()
{
    _comp_compgen -ax asciidoc doctype
}

_comp_cmd_asciidoc()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[abfdo]*)'
    # shellcheck disable=SC2254
    case $prev in
        --attribute | -${noargopts}a)
            return
            ;;
        --backend | -${noargopts}b)
            _comp_compgen -- -W 'docbook html4 xhtml11'
            return
            ;;
        --conf-file | -${noargopts}f)
            _comp_compgen_filedir conf
            return
            ;;
        --doctype | -${noargopts}d)
            _comp_xfunc_asciidoc_compgen_doctype
            return
            ;;
        --help | -${noargopts}h)
            _comp_compgen -- -W 'manpage syntax topics'
            return
            ;;
        --out-file | -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help manpage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_asciidoc asciidoc asciidoc.py

# ex: filetype=sh
