# bash completion for repomanage                           -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# yum-utils >= 1.1.24, use that instead.

_comp_cmd_repomanage()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    [[ $prev == -@([hk]|-help|-keep) ]] && return

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_repomanage repomanage

# ex: filetype=sh
