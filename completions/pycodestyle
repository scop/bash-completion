# pycodestyle completion                                   -*- shell-script -*-

_comp_cmd_pycodestyle()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -h | --help | --version)
            return
            ;;
        --format)
            _comp_compgen -- -W 'default pylint'
            return
            ;;
        --config)
            _comp_compgen_filedir
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
    complete -F _comp_cmd_pycodestyle pycodestyle

# ex: filetype=sh
