# kill(1) completion                                       -*- shell-script -*-

_comp_cmd_kill()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -s)
            _comp_compgen_signals
            return
            ;;
        -l | -n)
            return
            ;;
    esac

    if [[ $cword -eq 1 && $cur == -* ]]; then
        # return list of available signals
        _comp_compgen_signals -
        _comp_compgen -a help -c help "$1"
    else
        # return list of available PIDs and jobs
        _comp_compgen_pids
        _comp_compgen -ac "${cur#%}" -- -j -P %
    fi
} &&
    complete -F _comp_cmd_kill kill

# ex: filetype=sh
