# mussh(1) completion                                      -*- shell-script -*-

_comp_cmd_mussh()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | -V | -m | -t)
            return
            ;;
        -d)
            _comp_compgen -- -W '{0..2}'
            return
            ;;
        -v)
            _comp_compgen -- -W '{0..3}'
            return
            ;;
        -i | -H | -C)
            _comp_compgen_filedir
            return
            ;;
        -o | -po)
            _comp_compgen -x ssh options
            return
            ;;
        -l | -L)
            _comp_compgen -- -u
            return
            ;;
        -s)
            _comp_compgen_shells
            return
            ;;
        -p | -h)
            [[ $cur == *@* ]] && _comp_complete_user_at_host "$@" || _comp_compgen_known_hosts -a -- "$cur"
            return
            ;;
        -c)
            compopt -o filenames
            _comp_compgen_commands
            return
            ;;
    esac

    [[ $cur != -* ]] ||
        _comp_compgen_help
} &&
    complete -F _comp_cmd_mussh mussh

# ex: filetype=sh
