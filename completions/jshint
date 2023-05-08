# bash completion for jshint                               -*- shell-script -*-

_comp_cmd_jshint()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -v | --version | -h | --help | --exclude | --filename | -e | --extra-ext)
            return
            ;;
        -c | --config)
            _comp_compgen_filedir
            return
            ;;
        --reporter)
            _comp_compgen -- -W "jslint checkstyle unix"
            return
            ;;
        --extract)
            _comp_compgen -- -W "auto always never"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir js
} &&
    complete -F _comp_cmd_jshint jshint

# ex: filetype=sh
