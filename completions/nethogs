# bash completion for nethogs(8)                           -*- shell-script -*-

_comp_cmd_nethogs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        -d)
            # expect integer value
            _comp_compgen -aR -- -W '{0..9}'
            compopt -o nospace
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- -h
        return
    fi

    _comp_compgen_available_interfaces -a
} &&
    complete -F _comp_cmd_nethogs nethogs

# ex: filetype=sh
