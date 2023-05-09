# chpasswd(8) completion                                   -*- shell-script -*-

_comp_cmd_chpasswd()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[csR]*)'
    # shellcheck disable=SC2254
    case $prev in
        --crypt | -${noargopts}c)
            _comp_compgen -- -W 'DES MD5 NONE SHA256 SHA512'
            return
            ;;
        --sha-rounds | -${noargopts}s)
            return
            ;;
        --root | -${noargopts}R)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_chpasswd chpasswd

# ex: filetype=sh
