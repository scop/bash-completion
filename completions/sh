# POSIX sh(1) completion                                   -*- shell-script -*-

_comp_cmd_sh()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            return
            ;;
        -o | +o)
            _comp_compgen -- -W 'allexport errexit ignoreeof monitor noclobber
                noglob noexec nolog notify nounset verbose vi xtrace'
            return
            ;;
    esac

    local opts="-a -b -C -e -f -h -i -m -n -o -u -v -x"
    if [[ $cur == -* ]]; then
        _comp_compgen -- -W "$opts -c -s"
        return
    elif [[ $cur == +* ]]; then
        _comp_compgen -- -W "${opts//-/+}"
        return
    fi

    local REPLY ext=
    _comp_count_args -a "@(-c|[-+]o)"
    ((REPLY == 1)) && ext="sh"
    _comp_compgen_filedir $ext
} &&
    complete -F _comp_cmd_sh sh

# ex: filetype=sh
