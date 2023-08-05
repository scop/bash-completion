# bash completion for eject(1)                             -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_eject()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | --help | -V | --version | -c | --changerslot | -x | --cdspeed)
            return
            ;;
        -a | --auto | -i | --manualeject)
            _comp_compgen -- -W 'on off'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    elif [[ $prev == @(-d|--default) ]]; then
        return
    fi

    _comp_compgen_cd_devices
    _comp_compgen -a dvd_devices
} &&
    complete -F _comp_cmd_eject eject

# ex: filetype=sh
