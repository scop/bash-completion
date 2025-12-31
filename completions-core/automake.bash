# automake(1) completion                                   -*- shell-script -*-

_comp_cmd_automake()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case "$prev" in
        --help | --version)
            return
            ;;
        --warnings | -W)
            local cats=(gnu obsolete override portability syntax unsupported)
            _comp_compgen -- -W '"${cats[@]}" "${cats[@]/#/no-}" all none
                error'
            return
            ;;
        --libdir)
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

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_automake automake automake-1.1{0..6}

# ex: filetype=sh
