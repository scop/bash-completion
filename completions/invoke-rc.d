# invoke-rc.d(8) completion                                -*- shell-script -*-
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_comp_cmd_invoke_rc_d()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local sysvdir services options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    options=(--help --quiet --force --try-anyway --disclose-deny --query
        --no-fallback)

    if [[ $cword -eq 1 || $prev == --* ]]; then
        # generate valid_options
        _comp_compgen_split -- "$(
            tr " " "\n" <<<"${words[*]} ${options[*]}" |
                command sed -ne "/$(command sed 's/ /\\|/g' <<<"${options[*]}")/p" |
                sort | uniq -u
        )"
        _comp_expand_glob services '"$sysvdir"/!(README*|*.sh|$_comp_backup_glob)' &&
            _comp_compgen -a -- -W '"${services[@]#"$sysvdir"/}"'
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
