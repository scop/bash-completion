# pm-is-supported(1) completion                            -*- shell-script -*-

_comp_cmd_pm_is_supported()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen -- -W '--help --suspend --hibernate --suspend-hybrid'
} &&
    complete -F _comp_cmd_pm_is_supported pm-is-supported

# ex: filetype=sh
