# isql completion                                          -*- shell-script -*-
# by Victor Bogado da Silva Lins <victor@bogado.net>

_comp_cmd_isql()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    [[ -f ${ODBCINI-} ]] &&
        _comp_compgen_split -l -- "$(
            command sed -n 's/\]//g;s/^\[//gp' "$ODBCINI"
        )"
} &&
    complete -F _comp_cmd_isql isql

# ex: filetype=sh
