# bash completion for gssdp-discover/device-sniffer        -*- shell-script -*-

_comp_cmd_gssdp_discover()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --help | --target | --timeout | --rescan-interval | -[htnr])
            return
            ;;
        --interface | -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        --message-type | -m)
            [[ $1 == *gssdp-discover ]] || return
            local types=$("$1" --help 2>&1 |
                command sed -ne 's/^.*--message-type=.*(\([^)]*\))$/\1/p')
            _comp_compgen -F $' \t\n,' -- -W "$types"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_gssdp_discover gssdp-discover gssdp-device-sniffer

# ex: filetype=sh
