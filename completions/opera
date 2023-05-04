# opera(1) completion                                      -*- shell-script -*-

_comp_cmd_opera()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        ?(-)-widget | ?(-)-urllist | ?(-)-uiparserlog | ?(-)-uiwidgetsparserlog | \
            ?(-)-profilinglog)
            _comp_compgen_filedir
            return
            ;;
        ?(-)-[psb]d)
            _comp_compgen_filedir -d
            return
            ;;
        ?(-)-remote)
            _comp_compgen -- -W 'openURL\\( openFile\\( openM2\\(
                openComposer\\( addBookmark\\( raise\\(\\) lower\\(\\)'
            [[ ${COMPREPLY-} == *\( ]] && compopt -o nospace
            return
            ;;
        ?(-)-windowname)
            _comp_compgen -- -W 'first last opera{1..9}'
            return
            ;;
        ?(-)-geometry | ?(-)-window | ?(-)-display | ?(-)-urllistloadtimeout | \
            ?(-)-delaycustomizations | ?(-)-dialogtest | ?(-)-inidialogtest | \
            ?(-)-gputest)
            # argument required but no completions available
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir '@(?([xX]|[sS])[hH][tT][mM]?([lL]))'
} &&
    complete -F _comp_cmd_opera opera

# ex: filetype=sh
