# faillog(8) completion                                    -*- shell-script -*-

_comp_cmd_faillog()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[lmtu]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --lock-time | --maximum | --time | -${noargopts}[hlmt])
            return
            ;;
        --user | -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_faillog faillog

# ex: filetype=sh
