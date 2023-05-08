# monodevelop completion                                   -*- shell-script -*-

_comp_cmd_monodevelop()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_monodevelop monodevelop

# ex: filetype=sh
