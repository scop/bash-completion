# lrzip(1) completion                                      -*- shell-script -*-

_comp_cmd_lrzip()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local xspec="*.lrz"

    local noargopts='!(-*|*[SmwdoOLNp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --suffix | --maxram | --window | \
            -${noargopts}@([Smw]|[h?V]*))
            return
            ;;
        --decompress | -${noargopts}d)
            xspec="!"$xspec
            ;;
        --outfile | -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
        --outdir | -${noargopts}O)
            _comp_compgen_filedir -d
            return
            ;;
        --level | -${noargopts}L)
            _comp_compgen -- -W '{1..9}'
            return
            ;;
        --nice-level | -${noargopts}N)
            _comp_compgen -- -W '{-20..19}'
            return
            ;;
        --threads | -${noargopts}p)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_lrzip lrzip

# ex: filetype=sh
