# killall(1) completion                                    -*- shell-script -*-

[[ $OSTYPE == *@(linux|freebsd|darwin)* ]] || return 1

_comp_cmd_killall()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[Zoysu]*)'
    # shellcheck disable=SC2254
    case $prev in
        --context | --older-than | --younger-than | --version | -${noargopts}@([Zoy]|V*))
            return
            ;;
        --signal | -${noargopts}s)
            _comp_compgen_signals
            return
            ;;
        --user | -${noargopts}u)
            _comp_compgen_allowed_users
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        ((cword == 1)) && _comp_compgen -a signals -
        return
    fi

    _comp_compgen_pnames
} &&
    complete -F _comp_cmd_killall killall

# ex: filetype=sh
