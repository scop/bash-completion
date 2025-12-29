# mii-tool(8) completion                                   -*- shell-script -*-

_comp_cmd_mii_tool()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[FA]*)'
    # shellcheck disable=SC2254
    case $prev in
        --force | -${noargopts}F)
            _comp_compgen -- -W '100baseTx-FD 100baseTx-HD 10baseT-FD
                10baseT-HD'
            return
            ;;
        --advertise | -${noargopts}A)
            _comp_compgen -- -W '100baseT4 100baseTx-FD 100baseTx-HD 10baseT-FD
                10baseT-HD'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_available_interfaces -a
    fi
} &&
    complete -F _comp_cmd_mii_tool -o default mii-tool

# ex: filetype=sh
