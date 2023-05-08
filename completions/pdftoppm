# bash completion for pdftoppm(1)                          -*- shell-script -*-

_comp_cmd_pdftoppm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -[flrxyWH] | -r[xy] | -scale?(-to-[xy]) | -jpegopt | -[ou]pw)
            return
            ;;
        -tiffcompression)
            _comp_compgen -- -W 'none packbits jpeg lzw deflate'
            return
            ;;
        -freetype | -aa | -aaVector)
            _comp_compgen -- -W 'yes no'
            return
            ;;
        -thinlinemode)
            _comp_compgen -- -W 'none solid shape'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    [[ $prev == *.pdf ]] || _comp_compgen_filedir pdf
} &&
    complete -F _comp_cmd_pdftoppm pdftoppm

# ex: filetype=sh
