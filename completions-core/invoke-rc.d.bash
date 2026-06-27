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

    local sysvdir
    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    if [[ -x $sysvdir/$prev ]]; then
        _comp_compgen_split -- "$(command sed -e 'y/|/ /' \
            -ne 's/^.*Usage:[ ]*[^ ]*[ ]*{*\([^}"]*\).*$/\1/p' \
            "$sysvdir/$prev")"
    else
        COMPREPLY=()
    fi

} &&
    complete -F _comp_cmd_invoke_rc_d invoke-rc.d
