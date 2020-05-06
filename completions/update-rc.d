# update-rc.d(8) completion                                -*- shell-script -*-
#
# Copyright (C) 2004 Servilio Afre Puentes <servilio@gmail.com>

_update_rc_d()
{
    local cur prev words cword
    _init_completion || return

    local sysvdir services options

    [[ -d /etc/rc.d/init.d ]] && sysvdir=/etc/rc.d/init.d ||
        sysvdir=/etc/init.d

    services=($(printf '%s ' $sysvdir/!(README*|*.sh|$_backup_glob)))
    services=(${services[@]#$sysvdir/})
    options=(-f -n)

    if [[ $cword -eq 1 || $prev == -* ]]; then
        COMPREPLY=($(compgen -W '${options[@]} ${services[@]}' \
            -X '$(tr " " "|" <<<${words[@]})' -- "$cur"))
    elif [[ $prev == ?($(tr " " "|" <<<"${services[*]}")) ]]; then
        COMPREPLY=($(compgen -W 'remove defaults start stop' -- "$cur"))
    elif [[ $prev == defaults && $cur == [0-9] ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
    elif [[ $prev == defaults && $cur == [sk]?([0-9]) ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
    elif [[ $prev == defaults && -z $cur ]]; then
        COMPREPLY=(0 1 2 3 4 5 6 7 8 9 s k)
    elif [[ $prev == ?(start|stop) ]]; then
        if [[ $cur == [0-9] || -z $cur ]]; then
            COMPREPLY=(0 1 2 3 4 5 6 7 8 9)
        elif [[ $cur == [0-9][0-9] ]]; then
            COMPREPLY=($cur)
        else
            COMPREPLY=()
        fi
    elif [[ $prev == ?([0-9][0-9]|[0-6S]) ]]; then
        if [[ -z $cur ]]; then
            if [[ $prev == [0-9][0-9] ]]; then
                COMPREPLY=(0 1 2 3 4 5 6 S)
            else
                COMPREPLY=(0 1 2 3 4 5 6 S .)
            fi
        elif [[ $cur == [0-6S.] ]]; then
            COMPREPLY=($cur)
        else
            COMPREPLY=()
        fi
    elif [[ $prev == "." ]]; then
        COMPREPLY=($(compgen -W "start stop" -- "$cur"))
    else
        COMPREPLY=()
    fi
} &&
    complete -F _update_rc_d update-rc.d

# ex: filetype=sh
