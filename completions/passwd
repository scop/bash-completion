# passwd(1) completion                                     -*- shell-script -*-

_comp_cmd_passwd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[nxwi]*)'
    # shellcheck disable=SC2254
    case $prev in
        --minimum | --maximum | --warning | --inactive | --help | --usage | \
            -${noargopts}[nxwi?])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    _comp_compgen_allowed_users
} &&
    complete -F _comp_cmd_passwd passwd

# ex: filetype=sh
