# invoke-rc.d(8) completion
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_comp_cmd_invoke_rc_d()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local sysvdir options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    options=(--help --quiet --force --try-anyway --disclose-deny --query
        --no-fallback)

    if [[ $cword -eq 1 || $prev == --* ]]; then
        # generate valid_options
        local IFS='|'
        local exclude="@(${words[*]})"
        _comp_unlocal IFS
        _comp_compgen -- -W '"${options[@]}"' -X "$exclude"
        # shellcheck disable=SC2154
        _comp_compgen -aC "$sysvdir" -- -f -X "@(README*|*.sh|$_comp_backup_glob)"
    elif [[ -x $sysvdir/$prev ]]; then
        _comp_compgen_split -- "$(command sed -e 'y/|/ /' \
            -ne 's/^.*Usage:[ ]*[^ ]*[ ]*{*\([^}"]*\).*$/\1/p' \
            "$sysvdir/$prev")"
    fi

} &&
    complete -F _comp_cmd_invoke_rc_d invoke-rc.d
