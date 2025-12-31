# lastlog(8) completion                                    -*- shell-script -*-

_comp_cmd_lastlog()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[btu]*)'
    # shellcheck disable=SC2254
    case $prev in
        --before | --help | --time | -${noargopts}@([bt]|h*))
            return
            ;;
        --user | -${noargopts}u)
            _comp_compgen -- -u
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_lastlog lastlog

# ex: filetype=sh
