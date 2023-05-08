# dumpe2fs(8) completion                                   -*- shell-script -*-

_comp_cmd_dumpe2fs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[oV])
            return
            ;;
        -*i)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    _comp_compgen -c "${cur:-/dev/}" filedir
} &&
    complete -F _comp_cmd_dumpe2fs dumpe2fs

# ex: filetype=sh
