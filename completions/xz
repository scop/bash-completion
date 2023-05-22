# xz(1) completion                                         -*- shell-script -*-

_comp_cmd_xz()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local xspec="*.@(xz|lzma|txz|tlz)"

    local noargopts='!(-*|*[CFTMS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --decompress | --list | --test | -${noargopts}[dlt]*)
            xspec="!"$xspec
            ;;
        --files | --files0)
            _comp_compgen_filedir
            return
            ;;
        --check | -${noargopts}C)
            _comp_compgen -- -W 'crc32 crc64 sha256 none'
            return
            ;;
        --format | -${noargopts}F)
            _comp_compgen -- -W 'auto xz lzma raw'
            return
            ;;
        --threads | -${noargopts}T)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{0..$REPLY}"
            return
            ;;
        --memlimit | --memlimit-compress | --memlimit-decompress | --memory | \
            --suffix | --delta | --lzma1 | --lzma2 | -${noargopts}[MS])
            return
            ;;
        --help | --long-help | --version | --info-memory | -${noargopts}[hHV])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --long-help
        _comp_compgen -a -- -W '{-1..-9}'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_xz xz pxz

# ex: filetype=sh
