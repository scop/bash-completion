# lpr(1) completion                                        -*- shell-script -*-

_comp_cmd_lpr()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -P)
            _comp_compgen_split -- "$(lpstat -a 2>/dev/null | cut -d' ' -f1)"
            return
            ;;
        -U)
            _comp_compgen -- -u
            return
            ;;
        -o)
            _comp_compgen -- -W "media= landscape orientation-requested= sides= fitplot number-up= scaling= cpi= lpi= page-bottom= page-top= page-left= page-right="
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            return
            ;;
    esac

    if [[ $cur == - ]]; then
        _comp_compgen -- -W '-E -H -C -J -T -P -U -h -l -m -o -p -q -r'
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_lpr lpr

# ex: filetype=sh
