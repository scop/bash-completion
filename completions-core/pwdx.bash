# pwdx(1) completion                                       -*- shell-script -*-

_comp_cmd_pwdx()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | -V | --version)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help ||
            _comp_compgen -- -W '-V'
    else
        _comp_compgen_pids
    fi
} &&
    complete -F _comp_cmd_pwdx pwdx

# ex: filetype=sh
