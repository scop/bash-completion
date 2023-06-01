# filesnarf etc completion                                 -*- shell-script -*-

_comp_cmd_snarf()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    fi

} &&
    complete -F _comp_cmd_snarf filesnarf mailsnarf msgsnarf

# ex: filetype=sh
