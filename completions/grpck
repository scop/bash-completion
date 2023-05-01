# grpck(8) completion                                      -*- shell-script -*-

_comp_cmd_grpck()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[R]*)'
    # shellcheck disable=SC2254
    case $prev in
        --root | -${noargopts}R)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_grpck grpck

# ex: filetype=sh
