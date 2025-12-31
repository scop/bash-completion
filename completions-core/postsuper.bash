# postsuper(1) completion                                  -*- shell-script -*-

_comp_cmd_postsuper()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            _comp_compgen_filedir -d
            return
            ;;
        -[dr])
            _comp_compgen_split -- "ALL $(mailq 2>/dev/null |
                command sed -e '1d; $d; /^[^0-9A-Z]/d; /^$/d; s/[* !].*$//')"
            return
            ;;
        -h)
            _comp_compgen_split -- "ALL $(mailq 2>/dev/null |
                command sed \
                    -e '1d; $d; /^[^0-9A-Z]/d; /^$/d; s/[* ].*$//; /!$/d')"
            return
            ;;
        -H)
            _comp_compgen_split -- "ALL $(mailq 2>/dev/null | command sed \
                -e '1d; $d; /^[^0-9A-Z]/d; /^$/d; /^[0-9A-Z]*[* ]/d; s/!.*$//')"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen -- -W 'hold incoming active deferred'
} &&
    complete -F _comp_cmd_postsuper postsuper

# ex: filetype=sh
