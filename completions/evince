# evince(1) completion                                     -*- shell-script -*-

_comp_cmd_evince()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[pil]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help* | --sm-client-id | --class | --name | --screen | --gdk-debug | \
            --gdk-no-debug | --gtk-module | --gtk-debug | --gtk-no-debug | --page-label | \
            --page-index | --find | --display | -${noargopts}[hpil])
            return
            ;;
        --sm-client-state-file)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir '@(@(?(e)ps|?(E)PS|[pf]df|[PF]DF|dvi|DVI)?(.gz|.GZ|.bz2|.BZ2|.xz|.XZ)|cb[7rtz]|djv?(u)|tif?(f)|?(o)xps)'
} &&
    complete -F _comp_cmd_evince evince

# ex: filetype=sh
