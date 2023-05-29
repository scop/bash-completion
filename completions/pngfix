# pngfix completion                                        -*- shell-script -*-

_comp_cmd_pngfix()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --suffix | --prefix)
            return
            ;;
        --output)
            _comp_compgen_filedir
            return
            ;;
        --strip)
            _comp_compgen_split -F '|' -- "$("$1" --help 2>&1 |
                command sed -ne 's/.*--strip=\[\([^]]*\)\].*/\1/p')"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir png
} &&
    complete -F _comp_cmd_pngfix pngfix

# ex: filetype=sh
