# gpgv(1) completion                                       -*- shell-script -*-

_comp_cmd_gpgv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version | --weak-digest | --*-fd | -!(-*)[?h]*)
            return
            ;;
        --keyring)
            _comp_compgen_filedir "@(gpg|kbx)"
            return
            ;;
        --homedir)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    local REPLY
    _comp_count_args -a "--@(weak-digest|*-fd|keyring|homedir)"
    local args=$REPLY

    if [[ $cur == -* && $args -eq 1 ]]; then
        _comp_compgen_help
        return
    fi

    if ((args > 1)); then
        if [[ ${COMP_LINE,,} == *.@(asc|sig|sign)\ * ]]; then
            # Detached signature, only complete one arbitrary file arg and -
            if ((args == 2)); then
                _comp_compgen -- -W '-'
                _comp_compgen -a filedir
            fi
        else
            _comp_compgen_filedir gpg
        fi
    else
        _comp_compgen_filedir "@(asc|gpg|sig|sign)"
    fi
} &&
    complete -F _comp_cmd_gpgv gpgv gpgv2

# ex: filetype=sh
