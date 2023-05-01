# sitecopy(1) completion                                   -*- shell-script -*-
# Copyright 2003 Eelco Lempsink <eelcolempsink@gmx.net>
#           2011 Raphaël Droz <raphael.droz+floss@gmail.com>
# License: GNU GPL v2 or later

_comp_cmd_sitecopy()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[dgrp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --debug | -${noargopts}d)
            _comp_compgen -- -W 'socket files rcfile ftp http httpbody rsh sftp
                xml xmlparse cleartext'
            compopt -o nospace
            return
            ;;
        --logfile | --rcfile | -${noargopts}[gr])
            _comp_compgen_filedir
            return
            ;;
        --storepath | -${noargopts}p)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    case $cur in
        --*)
            _comp_compgen_help
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            return
            ;;

        # only complete long options
        -)
            compopt -o nospace
            COMPREPLY=(--)
            return
            ;;
    esac

    if [[ -r ~/.sitecopyrc ]]; then
        _comp_compgen_split -- "$("$1" -v |
            command sed -n '/^Site:/s/Site: //p')"
    fi
} &&
    complete -F _comp_cmd_sitecopy -o default sitecopy

# ex: filetype=sh
