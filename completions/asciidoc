# asciidoc(1) completion                                   -*- shell-script -*-

_asciidoc_doctype()
{
    COMPREPLY+=( $( compgen -W 'article book manpage' -- "$cur" ) )
}

_asciidoc()
{
    local cur prev words cword split
    _init_completion -s || return

    case $prev in
        --attribute|-a)
            return
            ;;
        --backend|-b)
            COMPREPLY=( $( compgen -W 'docbook html4 xhtml11' -- "$cur" ) )
            return
            ;;
        --conf-file|-f)
            _filedir conf
            return
            ;;
        --doctype|-d)
            _asciidoc_doctype
            return
            ;;
        --help|-h)
            COMPREPLY=( $( compgen -W 'manpage syntax topics' -- "$cur" ) )
            return
            ;;
        --out-file|-o)
            _filedir
            return
            ;;
    esac

    $split && return

    if [[ $cur == -* ]]; then
        COMPREPLY=( $( compgen -W '$( _parse_help "$1" "--help manpage" )' \
            -- "$cur" ) )
        [[ $COMPREPLY == *= ]] && compopt -o nospace
        return
    fi

    _filedir
} &&
complete -F _asciidoc asciidoc asciidoc.py

# ex: ts=4 sw=4 et filetype=sh
