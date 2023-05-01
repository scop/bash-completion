# hexdump(1) completion                                    -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_hexdump()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -V | -e | -n | -s)
            return
            ;;
        -f)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_hexdump hexdump hd

# ex: filetype=sh
