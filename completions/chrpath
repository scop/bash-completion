# chrpath(1) completion                                    -*- shell-script -*-

_comp_cmd_chrpath()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[r]*)'
    # shellcheck disable=SC2254
    case $prev in
        --version | --help | -${noargopts}[vh])
            return
            ;;
        --replace | -${noargopts}r)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_chrpath chrpath

# ex: filetype=sh
