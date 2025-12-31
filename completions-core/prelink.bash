# prelink(8) completion                                    -*- shell-script -*-

_comp_cmd_prelink()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -'?' | --help | --usage | -V | --version | -r | --reloc-only)
            return
            ;;
        -b | --black-list | --dynamic-linker | --undo-output)
            _comp_compgen_filedir
            return
            ;;
        -c | --config-file)
            _comp_compgen_filedir conf
            return
            ;;
        -C | --cache)
            _comp_compgen_filedir cache
            return
            ;;
        --ld-library-path)
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
    complete -F _comp_cmd_prelink prelink

# ex: filetype=sh
