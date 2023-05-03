# munindoc completion                                      -*- shell-script -*-

_comp_cmd_munindoc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_split -- "$(command ls /usr/share/munin/plugins 2>/dev/null)"
} &&
    complete -F _comp_cmd_munindoc munindoc

# ex: filetype=sh
