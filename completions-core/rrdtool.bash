# bash completion for rrdtool                              -*- shell-script -*-

_comp_cmd_rrdtool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((${#words[@]} == 2)); then
        _comp_compgen -- -W 'create update updatev graph dump restore last
            lastupdate first info fetch tune resize xport'
    else
        _comp_compgen_filedir rrd
    fi
} &&
    complete -F _comp_cmd_rrdtool rrdtool

# ex: filetype=sh
