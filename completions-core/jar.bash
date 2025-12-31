# jar(1) completion                                        -*- shell-script -*-

_comp_cmd_jar()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'c t x u'
        return
    fi

    case ${words[1]} in
        *c*f)
            _comp_compgen_filedir
            ;;
        *f)
            _comp_compgen_filedir_xspec unzip
            ;;
        *)
            _comp_compgen_filedir
            ;;
    esac
} &&
    complete -F _comp_cmd_jar jar

# ex: filetype=sh
