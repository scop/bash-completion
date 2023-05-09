# Slackware Linux pkgtool completion                       -*- shell-script -*-

_comp_cmd_pkgtool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        --source_dir | --target_dir)
            _comp_compgen_filedir -d
            return
            ;;
        --sets)
            # argument required but no completions available
            return
            ;;
        --source_device)
            _comp_compgen -c "${cur:-/dev/}" -- -f -d
            return
            ;;
        --tagfile)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--sets --ignore-tagfiles --tagfile
            --source-mounted --source_dir --target_dir --source_device'
    fi
} &&
    complete -F _comp_cmd_pkgtool pkgtool

# ex: filetype=sh
