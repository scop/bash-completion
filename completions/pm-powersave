# pm-powersave(8) completion                               -*- shell-script -*-

_comp_cmd_pm_powersave()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen -- -W "true false"
} &&
    complete -F _comp_cmd_pm_powersave pm-powersave

# ex: filetype=sh
