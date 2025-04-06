# Slackware Linux upgradepkg completion                    -*- shell-script -*-

_comp_cmd_upgradepkg()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--dry-run --install-new --reinstall --verbose'
        return
    fi

    if [[ $cur =~ ^[^%]+% ]]; then
        local prefix=$BASH_REMATCH nofiles=""
        compopt -o filenames
        _comp_compgen -P "$prefix" -- -f -X "!*.t[bgxl]z" || nofiles=set
        _comp_compgen -aP "$prefix" -- -S '/' -d
        [[ $nofiles ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir 't[bglx]z'
} &&
    complete -F _comp_cmd_upgradepkg upgradepkg

# ex: filetype=sh
