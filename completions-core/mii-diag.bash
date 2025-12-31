# mii-diag(8) completion                                   -*- shell-script -*-

_comp_cmd_mii_diag()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -F | -A | --advertise | --fixed-speed)
            _comp_compgen -- -W '100baseT4 100baseTx 100baseTx-FD 100baseTx-HD
                10baseT 10baseT-FD 10baseT-HD'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen_available_interfaces -a
    fi
} &&
    complete -F _comp_cmd_mii_diag -o default mii-diag

# ex: filetype=sh
