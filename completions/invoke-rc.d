# invoke-rc.d(8) completion                                -*- shell-script -*-
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_invoke_rc_d()
{
    local cur prev words cword
    _init_completion || return

    local sysvdir services options valid_options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d \
        || sysvdir=/etc/init.d

    services=( $(printf '%s ' $sysvdir/!(README*|*.sh|$_backup_glob)) )
    services=( ${services[@]#$sysvdir/} )
    options=( --help --quiet --force --try-anyway --disclose-deny --query \
        --no-fallback )

    if [[ ($cword -eq 1) || ("$prev" == --* ) ]]; then
    valid_options=( $(\
        tr " " "\n" <<<"${words[*]} ${options[*]}" \
        | command sed -ne "/$(command sed "s/ /\\\\|/g" <<<"${options[*]}")/p" \
        | sort | uniq -u \
        ) )
    COMPREPLY=( $(compgen -W '${valid_options[@]} ${services[@]}' -- "$cur") )
    elif [[ -x $sysvdir/$prev ]]; then
        COMPREPLY=( $(compgen -W '`command sed -e "y/|/ /" \
            -ne "s/^.*Usage:[ ]*[^ ]*[ ]*{*\([^}\"]*\).*$/\1/p" \
            $sysvdir/$prev`' -- "$cur") )
    else
        COMPREPLY=()
    fi

} &&
complete -F _invoke_rc_d invoke-rc.d

# ex: filetype=sh
