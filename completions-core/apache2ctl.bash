# apache2ctl(1) completion                                 -*- shell-script -*-

_comp_cmd_apache2ctl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local APWORDS
    APWORDS=$("$1" 2>&1 >/dev/null | _comp_awk 'NR<2 { print $3; exit }' |
        tr "|" " ")

    _comp_compgen -- -W "$APWORDS"
} &&
    complete -F _comp_cmd_apache2ctl apache2ctl

# ex: filetype=sh
