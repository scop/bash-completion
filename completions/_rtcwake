# bash completion for rtcwake                              -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# util-linux >= 2.23, use that instead.

_comp_cmd_rtcwake()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case "$prev" in
        --help | -h | --version | -V | --seconds | -s | --time | -t)
            return
            ;;
        --mode | -m)
            _comp_compgen -- -W 'standby mem disk on no off'
            return
            ;;
        --device | -d)
            _comp_expand_glob COMPREPLY '/dev/rtc?*' &&
                _comp_compgen -- -W '"${COMPREPLY[@]#/dev/}"'
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
} &&
    complete -F _comp_cmd_rtcwake rtcwake

# ex: filetype=sh
