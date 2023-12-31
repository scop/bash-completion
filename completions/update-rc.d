# update-rc.d(8) completion                                -*- shell-script -*-
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_comp_cmd_update_rc_d()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local sysvdir services options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    _comp_expand_glob services '"$sysvdir"/!(README*|*.sh|$_comp_backup_glob)' &&
        services=("${services[@]#$sysvdir/}")
    options=(-f -n)

    if [[ $cword -eq 1 || $prev == -* ]]; then
        _comp_compgen -- -W '"${options[@]}" ${services[@]+"${services[@]}"}' \
            -X '$(tr " " "|" <<<${words[@]})'
    elif ((${#services[@]})) && [[ $prev == ?($(tr " " "|" <<<"${services[*]}")) ]]; then
        _comp_compgen -- -W 'remove defaults start stop'
    elif [[ $prev == defaults && $cur == [0-9] ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
    elif [[ $prev == defaults && $cur == [sk]?([0-9]) ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
    elif [[ $prev == defaults && ! $cur ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9 s k)
    elif [[ $prev == ?(start|stop) ]]; then
        if [[ $cur == [0-9] || ! $cur ]]; then
            COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
        elif [[ $cur == [0-9][0-9] ]]; then
            COMPREPLY=("$cur")
        else
            COMPREPLY=()
        fi
    elif [[ $prev == ?([0-9][0-9]|[0-6S]) ]]; then
        if [[ ! $cur ]]; then
            if [[ $prev == [0-9][0-9] ]]; then
                COMPREPLY=(0 1 2 3 4 5 6 S)
            else
                COMPREPLY=(0 1 2 3 4 5 6 S .)
            fi
        elif [[ $cur == [0-6S.] ]]; then
            COMPREPLY=("$cur")
        else
            COMPREPLY=()
        fi
    elif [[ $prev == "." ]]; then
        _comp_compgen -- -W "start stop"
    else
        COMPREPLY=()
    fi
} &&
    complete -F _comp_cmd_update_rc_d update-rc.d

# ex: filetype=sh
