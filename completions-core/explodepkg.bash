# Slackware Linux explodepkg completion

_comp_cmd_explodepkg()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_filedir 't[bglx]z'
} &&
    complete -F _comp_cmd_explodepkg explodepkg
