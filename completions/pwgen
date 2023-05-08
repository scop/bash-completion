# pwgen(1) completion                                      -*- shell-script -*-

_comp_cmd_pwgen()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[NH]*)'
    # shellcheck disable=SC2254
    case $prev in
        --num-passwords | --help | -${noargopts}[Nh])
            return
            ;;
        --sha1 | -${noargopts}H)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_pwgen pwgen

# ex: filetype=sh
