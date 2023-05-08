# gpasswd(1) completion                                    -*- shell-script -*-

_comp_cmd_gpasswd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[adAM]*)'
    # shellcheck disable=SC2254
    case $prev in
        --add | --delete | --administrators | --members | -${noargopts}[adAM])
            _comp_compgen -- -u
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        # TODO: only -A and -M can be combined
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -g
} &&
    complete -F _comp_cmd_gpasswd gpasswd

# ex: filetype=sh
