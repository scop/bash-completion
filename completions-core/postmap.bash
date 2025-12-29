# postalias(1) and postmap(1) completion                   -*- shell-script -*-

_comp_cmd_postmap()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            _comp_compgen_filedir -d
            return
            ;;
        -[dq])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    if [[ $cur == *:* ]]; then
        compopt -o filenames
        _comp_compgen -c "${cur#*:}" -- -f
    else
        local len=${#cur} pval
        for pval in $(/usr/sbin/postconf -m 2>/dev/null); do
            if [[ $cur == "${pval:0:len}" ]]; then
                COMPREPLY+=("$pval:")
            fi
        done
        if [[ ! ${COMPREPLY-} ]]; then
            compopt -o filenames
            _comp_compgen -- -f
        fi
    fi
} &&
    complete -F _comp_cmd_postmap postmap postalias

# ex: filetype=sh
