# radvdump(8) completion                                   -*- shell-script -*-

_comp_cmd_radvdump()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | -v | --version)
            return
            ;;
        -d | --debug)
            _comp_compgen -- -W '{1..4}'
            return
            ;;
    esac

    _comp_compgen_usage -- --help
} &&
    complete -F _comp_cmd_radvdump radvdump

# ex: filetype=sh
