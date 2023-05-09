# tsig-keygen(8) completion                                -*- shell-script -*-

_comp_cmd_tsig_keygen()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h)
            return
            ;;
        -a)
            _comp_compgen -- -W 'hmac-{md5,sha{1,224,256,384,512}}'
            return
            ;;
        -r)
            _comp_compgen -- -W keyboard
            _comp_compgen -a filedir
            return
            ;;
    esac

    [[ $cur != -* ]] ||
        _comp_compgen_help
} &&
    complete -F _comp_cmd_tsig_keygen tsig-keygen

# ex: filetype=sh
