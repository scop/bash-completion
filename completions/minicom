# bash completion for minicom                              -*- shell-script -*-

_comp_cmd_minicom()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[acSCp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --attrib | --color | -${noargopts}[ac])
            _comp_compgen -- -W 'on off'
            return
            ;;
        --script | --capturefile | -${noargopts}[SC])
            _comp_compgen_filedir
            return
            ;;
        --ptty | -${noargopts}p)
            _comp_expand_glob COMPREPLY '/dev/tty*' &&
                _comp_compgen -- -W '"${COMPREPLY[@]}" "${COMPREPLY[@]#/dev/}"'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local -a files
    _comp_expand_glob files '{/etc/,/etc/minicom/,~/.}minirc.?*' &&
        _comp_compgen -- -W '"${files[@]##*minirc.}"'
} &&
    complete -F _comp_cmd_minicom -o default minicom

# ex: filetype=sh
