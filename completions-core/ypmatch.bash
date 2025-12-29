# bash completion for yp-tools                             -*- shell-script -*-

_comp_cmd_ypmatch()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local map cmd=${1##*/}

    [[ $cmd == ypcat && $cword -gt 1 ]] && return
    [[ $cmd == ypmatch && $cword -gt 2 ]] && return

    if [[ $cmd == ypmatch && $cword -eq 1 && ${#words[@]} -eq 3 ]]; then
        map=${words[2]}
        _comp_compgen_split -- "$(ypcat "$map" 2>/dev/null | cut -d':' -f 1)"
    else
        [[ $cmd == ypmatch && $cword -ne 2 ]] && return
        _comp_compgen_split -- "$(ypcat -x 2>/dev/null | cut -d'"' -f 2)"
    fi
} &&
    complete -F _comp_cmd_ypmatch ypmatch ypcat

# ex: filetype=sh
