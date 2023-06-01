# ngrep(8) completion                                      -*- shell-script -*-

_comp_cmd_ngrep()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -V | -n | -A | -s | -S | -c | -P)
            return
            ;;
        -I | -O)
            _comp_compgen_filedir 'pcap?(ng)'
            return
            ;;
        -d)
            _comp_compgen_available_interfaces -a
            _comp_compgen -a -- -W 'any'
            return
            ;;
        -W)
            _comp_compgen -- -W 'normal byline single none'
            return
            ;;
        -F)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi
} &&
    complete -F _comp_cmd_ngrep ngrep

# ex: filetype=sh
