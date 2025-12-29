# bash completion for resolvconf                           -*- shell-script -*-

_comp_cmd_resolvconf()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -a | -d)
            _comp_compgen_available_interfaces
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-a -d -u'
    fi
} &&
    complete -F _comp_cmd_resolvconf resolvconf

# ex: filetype=sh
