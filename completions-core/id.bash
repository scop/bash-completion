# id(1) completion                                         -*- shell-script -*-

_comp_cmd_id()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_help ||
            _comp_compgen -- -W '-G -g -u' # POSIX fallback
    else
        _comp_compgen -- -u
    fi
} &&
    complete -F _comp_cmd_id id

# ex: filetype=sh
