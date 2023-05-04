# dmesg(1) completion                                      -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_dmesg()
{
    [[ $OSTYPE == *solaris* ]] && return # no args there

    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | -V | --version | -s | --buffer-size | -M | -N)
            return
            ;;
        -f | --facility)
            _comp_compgen -- -W 'kern user mail daemon auth syslog lpr news'
            return
            ;;
        -l | --level | -n | --console-level)
            _comp_compgen -- -W '{1..8}'
            return
            ;;
    esac

    _comp_compgen_help || _comp_compgen_usage
} &&
    complete -F _comp_cmd_dmesg dmesg

# ex: filetype=sh
