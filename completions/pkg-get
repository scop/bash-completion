# pkg-get.completion completion                            -*- shell-script -*-
#
# Copyright 2006 Yann Rouillard <yann@opencsw.org>

_comp_cmd_pkg_get__catalog_file()
{
    local url="$1"
    local i conffile

    for file in /etc/opt/csw/pkg-get.conf /opt/csw/etc/pkg-get.conf /etc/pkg-get.conf; do
        if [[ -f $file ]]; then
            conffile="$file"
            break
        fi
    done
    conffile="${conffile:-/opt/csw/etc/pkg-get.conf}"

    if [[ ! $url ]]; then
        url=$(_comp_awk -F = ' $1=="url" { print $2 }' "$conffile")
    fi

    REPLY="${url##*//}"
    REPLY="${REPLY%%/*}"
    REPLY="/var/pkg-get/catalog-$REPLY"
} &&
    _comp_cmd_pkg_get()
    {
        local cur prev file url command=""
        COMPREPLY=()
        cur="${COMP_WORDS[COMP_CWORD]}"
        prev="${COMP_WORDS[COMP_CWORD - 1]}"

        if [[ ${prev} == "-s" ]]; then
            return 1
        fi

        local i=${#COMP_WORDS[*]}
        while ((i > 0)); do
            if [[ ${COMP_WORDS[--i]} == -s ]]; then
                url="${COMP_WORDS[i + 1]}"
            fi
            if [[ ${COMP_WORDS[i]} == @(-[aDdiUu]|available|describe|download|install|list|updatecatalog|upgrade) ]]; then
                command="${COMP_WORDS[i]}"
            fi
        done

        if [[ $command ]]; then
            if [[ $command == @(-[Ddi]|describe|download|install) ]]; then
                local REPLY
                _comp_cmd_pkg_get__catalog_file "$url"
                if [[ -f $REPLY ]]; then
                    local packages_list=$(_comp_awk '$0 ~ /BEGIN PGP SIGNATURE/ { exit } $1 ~ /^Hash:/ || $1 ~ /^ *(-|#|$)/ { next } { print $1 }' "$REPLY")
                    _comp_compgen -- -W "${packages_list}"
                fi
            fi
            return
        fi

        if [[ ${cur} == -* ]]; then
            local -a opts=(-c -d -D -f -i -l -s -S -u -U -v)
            _comp_compgen -- -W '"${opts[@]}"'
            return
        fi

        local -a commands=(
            available describe download install list updatecatalog upgrade
        )
        _comp_compgen -- -W '"${commands[@]}"'
    } &&
        complete -F _comp_cmd_pkg_get pkg-get

# ex: filetype=sh
