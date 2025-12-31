# bash completion for pdftotext(1)                         -*- shell-script -*-

_comp_cmd_pdftotext()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -help | --help | -'?' | -f | -l | -r | -x | -y | -W | -H | \
            -fixed | -opw | -upw)
            return
            ;;
        -enc)
            _comp_compgen_split -- "$("$1" -listenc 2>/dev/null |
                command sed -e 1d)"
            return
            ;;
        -eol)
            _comp_compgen -- -W "unix dos mac"
            return
            ;;
    esac

    if [[ $cur == -* && ${prev,,} != *.pdf ]]; then
        _comp_compgen_help
        return
    fi

    case ${prev,,} in
        - | *.txt) ;;
        *.pdf)
            _comp_compgen -- -W '-'
            _comp_compgen -a filedir txt
            ;;
        *) _comp_compgen_filedir pdf ;;
    esac
} &&
    complete -F _comp_cmd_pdftotext pdftotext

# ex: filetype=sh
