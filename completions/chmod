# chmod(1) completion                                      -*- shell-script -*-

_comp_cmd_chmod()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --help | --version)
            return
            ;;
        --reference)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    # Adapted from coreutils 8.28 chmod man page
    local modearg="-@(@(+([rwxXst])|[ugo])|+([0-7]))"

    # shellcheck disable=SC2053
    if [[ $cur == -* && $cur != $modearg ]]; then
        _comp_compgen_help || _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local REPLY
    _comp_count_args -i "$modearg"

    case $REPLY in
        1) ;; # mode
        *) _comp_compgen_filedir ;;
    esac
} &&
    complete -F _comp_cmd_chmod chmod

# ex: filetype=sh
