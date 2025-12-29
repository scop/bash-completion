# javaws(1) completion                                     -*- shell-script -*-

_comp_cmd_javaws()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    case $prev in
        -help | -license | -about | -viewer | -arg | -param | -property | -update | -umask)
            return
            ;;
        -basedir | -codebase)
            _comp_compgen_filedir -d
            return
            ;;
        -uninstall | -import)
            _comp_compgen_filedir jnlp
            return
            ;;
    esac

    if [[ $cur == *= ]]; then
        return
    elif [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir jnlp
} &&
    complete -F _comp_cmd_javaws javaws

# ex: filetype=sh
