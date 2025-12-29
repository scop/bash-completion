# cancel(1) completion                                     -*- shell-script -*-

_comp_cmd_cancel()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -U)
            return
            ;;
        -u)
            _comp_compgen -- -u
            return
            ;;
    esac

    _comp_compgen_split -- "$(lpstat 2>/dev/null | cut -d' ' -f1)"
} &&
    complete -F _comp_cmd_cancel cancel

# ex: filetype=sh
