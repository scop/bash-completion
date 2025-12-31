# pkgrm completion                                         -*- shell-script -*-
#
# Copyright 2006 Yann Rouillard <yann@opencsw.org>

_comp_cmd_pkgrm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # if a spool directory was given
    # we must complete with the package
    # available in this directory
    local spool=/var/sadm/pkg
    local i=$cword
    while ((i-- > 0)); do
        ((i--))
        case "${words[i]}" in
            -s)
                spool="${words[i + 1]}"
                break
                ;;
        esac
    done

    case $prev in
        -a | -V)
            _comp_compgen_filedir
            ;;
        -s | -R)
            _comp_compgen_filedir -d
            ;;
        -Y) ;;

        *)
            if [[ ${cur} == -* ]]; then
                local opts="-a -A -n -M -R -s -v -V -Y"
                _comp_compgen -- -W "${opts}"
            else
                _comp_compgen_split -- "$(/bin/ls -1 "$spool")"
            fi
            ;;
    esac
} &&
    complete -F _comp_cmd_pkgrm pkgrm

# ex: filetype=sh
