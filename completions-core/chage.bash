# chage(1) completion                                      -*- shell-script -*-

_comp_cmd_chage()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[dEImMWR]*)'
    # shellcheck disable=SC2254
    case $prev in
        --lastday | --expiredate | --help | --inactive | --mindays | --maxdays | \
            --warndays | -${noargopts}[dEhImMW])
            return
            ;;
        --root | -${noargopts}R)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -u
} &&
    complete -F _comp_cmd_chage chage

# ex: filetype=sh
