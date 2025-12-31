# postconf(1) completion                                   -*- shell-script -*-

_comp_cmd_postconf()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local eqext

    case $prev in
        -b | -t)
            _comp_compgen_filedir
            return
            ;;
        -c)
            _comp_compgen_filedir -d
            return
            ;;
        -e)
            cur=${cur#[\"\']}
            eqext='='
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    local len=${#cur} pval
    for pval in $(/usr/sbin/postconf 2>/dev/null | cut -d ' ' -f 1); do
        if [[ $cur == "${pval:0:len}" ]]; then
            COMPREPLY+=("$pval${eqext-}")
        fi
    done
} &&
    complete -F _comp_cmd_postconf postconf

# ex: filetype=sh
