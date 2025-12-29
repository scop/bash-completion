# vipw(8) and vigr completion                              -*- shell-script -*-

_comp_cmd_vipw()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[R]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | -${noargopts}h)
            return
            ;;
        --root | -${noargopts}R | -d)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    _comp_compgen_help || _comp_compgen_usage
} &&
    complete -F _comp_cmd_vipw vipw vigr

# ex: filetype=sh
