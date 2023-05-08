# pwd(1) completion                                        -*- shell-script -*-

_comp_cmd_pwd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version)
            return
            ;;
    esac

    _comp_compgen_usage -c help -s "$1"
} &&
    complete -F _comp_cmd_pwd pwd

# ex: filetype=sh
