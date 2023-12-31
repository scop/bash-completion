# invoke-rc.d(8) completion                                -*- shell-script -*-
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_comp_cmd_invoke_rc_d()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local sysvdir services options valid_options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    options=(--help --quiet --force --try-anyway --disclose-deny --query
        --no-fallback)

    if [[ $cword -eq 1 || $prev == --* ]]; then
        valid_options=($(
            tr " " "\n" <<<"${words[*]} ${options[*]}" |
                command sed -ne "/$(command sed 's/ /\\|/g' <<<"${options[*]}")/p" |
                sort | uniq -u
        ))
        ((${#valid_options[@]})) && COMPREPLY+=("${valid_options[@]}")
        services=($sysvdir/!(README*|*.sh|$_comp_backup_glob))
        services=(${services[@]#$sysvdir/})
        ((${#services[@]})) && COMPREPLY+=("${services[@]}")
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -W '"${COMPREPLY[@]}"'
    elif [[ -x $sysvdir/$prev ]]; then
        _comp_compgen_split -- "$(command sed -e 'y/|/ /' \
            -ne 's/^.*Usage:[ ]*[^ ]*[ ]*{*\([^}"]*\).*$/\1/p' \
            "$sysvdir/$prev")"
    else
        COMPREPLY=()
    fi

} &&
    complete -F _comp_cmd_invoke_rc_d invoke-rc.d

# ex: filetype=sh
