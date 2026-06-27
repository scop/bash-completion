# invoke-rc.d(8) completion
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_comp_cmd_invoke_rc_d()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local options
    options=(--help --quiet --force --try-anyway --disclose-deny --query
        --no-fallback)

    if [[ $cword -eq 1 || $prev == --* ]]; then
        # generate valid_options
        local IFS='|'
        local exclude="@(${words[*]})"
        _comp_unlocal IFS
        _comp_compgen -- -W '"${options[@]}"' -X "$exclude"
        _comp_compgen -a sysv_services
        return
    fi

    local sysvdirs
    if _comp_sysvdirs && [[ -x ${sysvdirs[0]}/$prev ]]; then
        _comp_compgen_split -- "$(command sed -e 'y/|/ /' \
            -ne 's/^.*Usage:[ ]*[^ ]*[ ]*{*\([^}"]*\).*$/\1/p' \
            "${sysvdirs[0]}/$prev")"
    else
        COMPREPLY=()
    fi

} &&
    complete -F _comp_cmd_invoke_rc_d invoke-rc.d
