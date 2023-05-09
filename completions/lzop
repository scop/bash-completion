# lzop(1) completion                                       -*- shell-script -*-

_comp_cmd_lzop()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[oS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --output | -${noargopts}o)
            _comp_compgen_filedir
            return
            ;;
        --path)
            _comp_compgen_filedir -d
            return
            ;;
        --suffix | -${noargopts}S)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-{1..9} -P
            --fast --best --decompress --extract --test --list --ls --info
            --sysinfo --license --help --version --stdout --output --path
            --force --no-checksum --no-name --name --no-mode --no-time --suffix
            --keep --delete --crc32 --no-warn --ignore-warn --quiet --verbose
            --no-stdin --filter --checksum --no-color --mono --color'
        return
    fi

    local xspec="*.?(t)lzo"
    case $prev in
        --decompress | --uncompress | --extract | --list | --ls | --info | --test)
            xspec="!"$xspec
            ;;
        --force)
            xspec=
            ;;
        --*) ;;

        -*f*)
            xspec=
            ;;
        -*[dltx]*)
            xspec="!"$xspec
            ;;
    esac

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_lzop lzop

# ex: filetype=sh
