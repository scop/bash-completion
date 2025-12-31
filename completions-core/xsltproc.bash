# xsltproc(1) completion                                   -*- shell-script -*-

_comp_cmd_xsltproc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --output | -o)
            _comp_compgen_filedir
            return
            ;;
        # TODO : number only
        --maxdepth)
            return
            ;;
        --encoding)
            # some aliases removed
            local encodings=$(iconv -l | command sed -e 's/\/.*//')
            _comp_compgen -- -X '@(UTF[1378]|8859|ISO[0-9_])*' -W '$encodings'
            return
            ;;
        --param | --stringparam)
            return
            ;;
        # not really like --writesubtree
        --path)
            _comp_compgen_filedir -d
            return
            ;;
        --writesubtree)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $cword -gt 2 && ${words[cword - 2]} == --?(string)param ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        COMPREPLY=("${COMPREPLY[@]%:}")
    else
        # TODO: 1st file xsl|xslt, 2nd XML
        _comp_compgen_filedir '@(xsl|xslt|xml|dbk|docbook|page)'
    fi
} &&
    complete -F _comp_cmd_xsltproc xsltproc

# ex: filetype=sh
