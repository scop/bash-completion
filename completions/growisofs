# growisofs(1) completion                                  -*- shell-script -*-

_comp_cmd_growisofs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -version | -speed)
            return
            ;;
        -Z | -M)
            compopt -o nospace
            _comp_compgen_dvd_devices
            return
            ;;
        /?(r)dev/*)
            if [[ $cur == =* ]]; then
                # e.g. /dev/dvd=foo.iso, /dev/dvdrw=/dev/zero
                _comp_compgen -c "${cur#=}" filedir
                return
            fi
            ;;
    esac

    if [[ $cur == -* ]]; then
        # TODO: mkisofs options
        _comp_compgen -- -W '-dvd-compat -overburn -speed= -Z -M'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_growisofs growisofs

# ex: filetype=sh
