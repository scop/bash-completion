# jpegoptim(1) completion                                  -*- shell-script -*-

_comp_cmd_jpegoptim()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[dmTS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV]*)
            return
            ;;
        --dest | -${noargopts}d)
            _comp_compgen_filedir -d
            return
            ;;
        --max | --threshold | -${noargopts}[mT])
            _comp_compgen -- -W '{0..100}'
            return
            ;;
        --size | -${noargopts}S)
            _comp_compgen -- -W '{1..99}%'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir 'jp?(e)g'
} &&
    complete -F _comp_cmd_jpegoptim jpegoptim

# ex: filetype=sh
