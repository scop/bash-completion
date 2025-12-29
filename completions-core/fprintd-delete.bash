# bash completion for fprintd-delete and fprintd-list      -*- shell-script -*-

_comp_cmd_fprintd_delete()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen_allowed_users
} &&
    complete -F _comp_cmd_fprintd_delete fprintd-delete fprintd-list

# ex: filetype=sh
