# uscan completion                                         -*- shell-script -*-

_comp_cmd_uscan()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --package)
            _comp_compgen -x apt-cache sources
            return
            ;;
        --watchfile)
            _comp_compgen_filedir
            return
            ;;
        --destdir)
            _comp_compgen_filedir -d
            return
            ;;
        --timeout | --upstream-version | --download-version | \
            --check-dirname-level | --check-dirname-regex)
            COMPREPLY=()
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
} &&
    complete -F _comp_cmd_uscan uscan

# ex: filetype=sh
