# tcpkill completion                                       -*- shell-script -*-

_comp_cmd_tcpkill()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*i)
            _comp_compgen_available_interfaces -a
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-i -1 -2 -3 -4 -5 -6 -7 -8 -9'
    fi

} &&
    complete -F _comp_cmd_tcpkill tcpkill

# ex: filetype=sh
