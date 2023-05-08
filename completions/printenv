# printenv(1) completion                                   -*- shell-script -*-

_comp_cmd_printenv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -v
} &&
    complete -F _comp_cmd_printenv printenv

# ex: filetype=sh
