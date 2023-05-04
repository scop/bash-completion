# Slackware Linux installpkg completion                    -*- shell-script -*-

_comp_cmd_installpkg()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        --root)
            _comp_compgen_filedir -d
            return
            ;;
        --priority)
            _comp_compgen -- -W 'ADD REC OPT SKP'
            return
            ;;
        --tagfile)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--warn --md5sum --root --infobox --terse --menu
            --ask --priority --tagfile'
        return
    fi

    _comp_compgen_filedir 't[bglx]z'
} &&
    complete -F _comp_cmd_installpkg installpkg

# ex: filetype=sh
