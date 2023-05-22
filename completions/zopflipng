# bash completion for zopflipng                            -*- shell-script -*-

_comp_cmd_zopflipng()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -h | --help)
            return
            ;;
        --splitting)
            _comp_compgen -- -W '{0..3}'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -R help -- -h
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -W '"${COMPREPLY[@]%:}"'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    if [[ ${words[*]} != *\ --prefix=* ]]; then
        # 2 png args only if --prefix not given
        local REPLY
        _comp_count_args
        ((REPLY < 3)) && _comp_compgen_filedir png
    else
        # otherwise arbitrary number of png args
        _comp_compgen_filedir png
    fi
} &&
    complete -F _comp_cmd_zopflipng zopflipng

# ex: filetype=sh
