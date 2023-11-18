# a2x(1) completion                                        -*- shell-script -*-

_comp_cmd_a2x()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[aDd]*)'
    # shellcheck disable=SC2254
    case $prev in
        --attribute | --asciidoc-opts | --dblatex-opts | --fop-opts | --help | \
            --version | --xsltproc-opts | -${noargopts}[ah])
            return
            ;;
        --destination-dir | --icons-dir | -${noargopts}D)
            _comp_compgen_filedir -d
            return
            ;;
        --doctype | -${noargopts}d)
            _comp_compgen -x asciidoc doctype
            return
            ;;
        --stylesheet)
            _comp_compgen_filedir css
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_a2x a2x

# ex: filetype=sh
