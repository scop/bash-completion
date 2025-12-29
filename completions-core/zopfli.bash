# bash completion for zopfli                               -*- shell-script -*-

_comp_cmd_zopfli()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -R help -- -h
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -W '"${COMPREPLY[@]%#}"'
        [[ ${COMPREPLY-} == --i ]] && compopt -o nospace
        return
    fi

    _comp_compgen_tilde && return

    local xspec="*.@(gz|t[ag]z)"
    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_zopfli zopfli

# ex: filetype=sh
