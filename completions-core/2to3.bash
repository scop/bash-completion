# bash completion for 2to3                                 -*- shell-script -*-

_comp_cmd_2to3()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -h | --help | --add-suffix)
            return
            ;;
        -f | --fix | -x | --nofix)
            _comp_compgen_split -- "$(
                "$1" --list-fixes 2>/dev/null | command sed -e 1d
            )"
            return
            ;;
        -j | --processes)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
        -o | --output-dir)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir py
} &&
    complete -F _comp_cmd_2to3 2to3

# ex: filetype=sh
