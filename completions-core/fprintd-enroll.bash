# bash completion for fprintd-enroll and fprintd-verify    -*- shell-script -*-

_comp_cmd_fprintd_enroll()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[f]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | -h)
            return
            ;;
        --finger | -${noargopts}f)
            # Only -enroll may output a message with valid options in it
            _comp_compgen_split -- "$(
                "${1/-verify/-enroll}" --finger no-such-finger 2>&1 |
                    command sed \
                        -e s/,//g -ne 's/^.*Name must be one of \(.*\)/\1/p'
            )"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    local REPLY
    _comp_count_args -a "@(--finger|-${noargopts}[f])"
    if ((REPLY == 1)); then
        _comp_compgen_allowed_users
    fi
} &&
    complete -F _comp_cmd_fprintd_enroll fprintd-enroll fprintd-verify

# ex: filetype=sh
