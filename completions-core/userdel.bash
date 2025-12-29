# userdel(8) completion                                    -*- shell-script -*-

_comp_cmd_userdel()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[R]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | -${noargopts}h)
            return
            ;;
        --root | -${noargopts}R)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -u
} &&
    complete -F _comp_cmd_userdel userdel

# ex: filetype=sh
