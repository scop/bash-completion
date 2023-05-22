# lzip(1) completion                                       -*- shell-script -*-

_comp_cmd_lzip()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local decompress=""

    local noargopts='!(-*|*[bmsSBdno]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --member-size | --match-length | --dictionary-size | \
            --volume-size | --data-size | -${noargopts}@([bmsSB]|[hV]*))
            return
            ;;
        --decompress | -${noargopts}d)
            decompress=set
            ;;
        --threads | -${noargopts}n)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
        --output | -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-{1..9}'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    if [[ $decompress ]]; then
        _comp_compgen_filedir lz
        return
    fi

    compopt -o filenames
    _comp_compgen -- -f -X "*.lz" -o plusdirs
} &&
    complete -F _comp_cmd_lzip clzip lzip pdlzip plzip

# ex: filetype=sh
