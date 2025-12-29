# bash completion for oggdec(1)                            -*- shell-script -*-

_comp_cmd_oggdec()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[beso]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV]*)
            return
            ;;
        --bits | -${noargopts}b)
            _comp_compgen -- -W "8 16"
            return
            ;;
        --endianness | --sign | -${noargopts}[es])
            _comp_compgen -- -W "0 1"
            return
            ;;
        --output | -${noargopts}o)
            _comp_compgen_filedir wav
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir ogg
} &&
    complete -F _comp_cmd_oggdec oggdec

# ex: filetype=sh
