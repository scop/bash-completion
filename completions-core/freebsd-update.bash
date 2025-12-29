# bash completion for FreeBSD update tool - freebsd-update -*- shell-script -*-

[[ $OSTYPE == *freebsd* ]] || return 1

_comp_cmd_freebsd_update()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -b | -d)
            _comp_compgen_filedir -d
            return
            ;;
        -f)
            _comp_compgen_filedir
            return
            ;;
        -k | -r | -s | -t)
            return
            ;;
    esac

    _comp_compgen -- -W 'fetch cron upgrade install rollback IDS'
} &&
    complete -F _comp_cmd_freebsd_update freebsd-update

# ex: filetype=sh
