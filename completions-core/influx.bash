# bash completion for influx(8)                            -*- shell-script -*-

_comp_cmd_influx()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -version | -port | -database | -password | -username | -execute | -pps)
            return
            ;;
        -host)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -format | -precision | -consistency)
            local args=$("$1" --help 2>&1 | _comp_awk "\$1 == \"$prev\" { print \$2 }")
            _comp_compgen -F $' \t\n'"\"'|" -- -W "$args"
            return
            ;;
        -import | -path)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $cur == -* ]] &&
        _comp_compgen_help
} &&
    complete -F _comp_cmd_influx influx

# ex: filetype=sh
