# bash completion for pm-utils                             -*- shell-script -*-

_comp_cmd_pm_hibernate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_help
    _comp_compgen -a -- -W '--help'
} &&
    complete -F _comp_cmd_pm_hibernate pm-hibernate pm-suspend pm-suspend-hybrid

# ex: filetype=sh
