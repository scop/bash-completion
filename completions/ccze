# ccze(1) completion                                       -*- shell-script -*-

_comp_cmd_ccze()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[acFmop]*)'
    # shellcheck disable=SC2254
    case $prev in
        -'?' | --help | --usage | -V | --version)
            return
            ;;
        --argument | --color | -${noargopts}[ac])
            # TODO?
            return
            ;;
        --rcfile | -${noargopts}F)
            _comp_compgen_filedir
            return
            ;;
        --mode | -${noargopts}m)
            _comp_compgen -- -W "curses ansi html"
            return
            ;;
        --option | -${noargopts}o)
            local -a opts=(scroll wordcolor lookups transparent cssfile)
            _comp_compgen -- -W '"${opts[@]}" "${opts[@]/#/no}"'
            return
            ;;
        --plugin | -${noargopts}p)
            _comp_compgen_split -- "$("$1" --list-plugins | command \
                sed -ne 's/^\([a-z0-9]\{1,\}\)[[:space:]]\{1,\}|.*/\1/p')"
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_ccze ccze

# ex: filetype=sh
