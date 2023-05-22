# bash completion for gzip                                 -*- shell-script -*-

_comp_cmd_gzip()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[bSACIJp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --blocksize | --suffix | --help | --version | --alias | --comment | \
            --iterations | --maxsplits | -${noargopts}[bShVACIJ])
            return
            ;;
        --processes | -${noargopts}p)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-{1..9}'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local xspec="*.@(gz|t[ag]z)"
    [[ ${1##*/} == pigz ]] && xspec="*.@([gz]z|t[ag]z)"

    if [[ $prev == --* ]]; then
        [[ $prev == --@(decompress|list|test) ]] && xspec="!"$xspec
        [[ $prev == --force ]] && xspec=
    elif [[ $prev == -* ]]; then
        [[ $prev == -*[dlt]* ]] && xspec="!"$xspec
        [[ $prev == -*f* ]] && xspec=
    fi

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_gzip gzip pigz

# ex: filetype=sh
