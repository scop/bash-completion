# newusers(8) completion                                   -*- shell-script -*-

_comp_cmd_newusers()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -c | --crypt)
            _comp_compgen -- -W 'DES MD5 NONE SHA256 SHA512'
            return
            ;;
        -s | --sha-rounds)
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
    complete -F _comp_cmd_newusers newusers

# ex: filetype=sh
