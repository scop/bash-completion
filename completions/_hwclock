# hwclock(8) completion                                    -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# util-linux >= 2.23, use that instead.

_comp_cmd_hwclock()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | -V | --version | --date | --epoch)
            return
            ;;
        -f | --rtc | --adjfile)
            _comp_compgen_filedir
            return
            ;;
    esac

    local PATH=$PATH:/sbin
    _comp_compgen_help
} &&
    complete -F _comp_cmd_hwclock hwclock

# ex: filetype=sh
