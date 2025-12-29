# munin-update completion                                  -*- shell-script -*-

_comp_cmd_munin_update()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --config)
            _comp_compgen_filedir
            return
            ;;
        --host)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--force-root --noforce-root --service --host
            --config --help --debug --nodebug --fork --nofork --stdout
            --nostdout --timeout'
    fi
} &&
    complete -F _comp_cmd_munin_update munin-update

# ex: filetype=sh
