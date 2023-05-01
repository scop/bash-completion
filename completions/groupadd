# groupadd(8) completion                                   -*- shell-script -*-

_comp_cmd_groupadd()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    # TODO: if -o/--non-unique is given, could complete on existing gids
    #       with -g/--gid

    local noargopts='!(-*|*[gKp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --gid | --key | --password | -${noargopts}[gKp])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_groupadd groupadd

# ex: filetype=sh
