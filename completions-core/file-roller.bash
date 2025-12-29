# file-roller(1) completion                                -*- shell-script -*-

_comp_cmd_file_roller()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local exts='@(7z?(.001)|ace|alz|ar|arj|[bglx]z|bz2|tb?(z)2|cab|cb[rz]|iso?(9660)|Z|t[abglx]z|cpio|deb|rar|?(g)tar|gem|lh[az]|lz[4h]|?(t)lrz|lzma|lzo|wim|swm|rpm|sit|zoo|?(t)zst)'

    local noargopts='!(-*|*[ae]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --help-all | --help-gtk | --help-sm-client | -${noargopts}'?')
            return
            ;;
        --sm-client-state-file)
            _comp_compgen_filedir
            return
            ;;
        --add-to | -${noargopts}a)
            _comp_compgen_filedir_xspec unzip
            _comp_compgen -a filedir "$exts"
            return
            ;;
        --extract-to | --default-dir | -${noargopts}e)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir_xspec unzip
    _comp_compgen -a filedir "$exts"
} &&
    complete -F _comp_cmd_file_roller file-roller

# ex: filetype=sh
