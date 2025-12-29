# snownews(1) completion                                   -*- shell-script -*-

_comp_cmd_snownews()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        # return list of available options
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_snownews snownews

# ex: filetype=sh
