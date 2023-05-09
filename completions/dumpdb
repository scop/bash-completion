# mailman dumpdb completion                                -*- shell-script -*-

_comp_cmd_dumpdb()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--marshal --pickle --noprint --help'
    else
        _comp_compgen_filedir
    fi

} &&
    complete -F _comp_cmd_dumpdb dumpdb

# ex: filetype=sh
