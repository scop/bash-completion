# bash completion for pydocstyle                           -*- shell-script -*-

_comp_cmd_pydocstyle()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --help | --version | --match | --ignore-decorators | --select | \
            --ignore | --add-select | --add-ignore | -!(-*)h)
            return
            ;;
        --config)
            _comp_compgen_filedir xml
            return
            ;;
        --convention)
            _comp_compgen -- -W "pep257 numpy"
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
    complete -F _comp_cmd_pydocstyle pydocstyle

# ex: filetype=sh
