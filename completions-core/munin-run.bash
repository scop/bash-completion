# munin-run completion                                     -*- shell-script -*-

_comp_cmd_munin_run()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --config | --sconffile)
            _comp_compgen_filedir
            return
            ;;
        --servicedir | --sconfdir)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen_split -- "$(command ls /etc/munin/plugins 2>/dev/null)"
    fi
} &&
    complete -F _comp_cmd_munin_run munin-run

# ex: filetype=sh
