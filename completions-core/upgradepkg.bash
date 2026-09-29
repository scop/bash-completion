# Slackware Linux upgradepkg completion

_comp_cmd_upgradepkg()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--dry-run --install-new --reinstall --verbose'
        return
    fi

    if [[ $cur =~ ^[^%]+% ]]; then
        local prefix=$BASH_REMATCH
        _comp_compgen -P "$prefix" filedir 't[bgxl]z'
        return
    fi

    _comp_compgen_filedir 't[bglx]z'
} &&
    complete -F _comp_cmd_upgradepkg upgradepkg
