# dsniff completion                                        -*- shell-script -*-

_comp_cmd_dsniff()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -r | -w | -f | -p)
            _comp_compgen_filedir
            return
            ;;
        -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        _comp_compgen -a -- -W '-r -w -p'
    fi

} &&
    complete -F _comp_cmd_dsniff dsniff

# ex: filetype=sh
