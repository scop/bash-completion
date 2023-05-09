# autoconf(1) completion                                   -*- shell-script -*-

_comp_cmd_autoconf()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case "$prev" in
        --help | -h | --version | -V | --trace | -t)
            return
            ;;
        --output | -o)
            _comp_compgen_filedir
            return
            ;;
        --warnings | -W)
            local cats=(cross obsolete syntax)
            _comp_compgen -- -W '"${cats[@]}" "${cats[@]/#/no-}" all none
                error'
            return
            ;;
        --prepend-include | -B | --include | -I)
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

    _comp_compgen_filedir '@(ac|in)'
} &&
    complete -F _comp_cmd_autoconf autoconf

# ex: filetype=sh
