# pkg-get.completion completion
#
# Copyright 2006 Yann Rouillard <yann@opencsw.org>

_comp_cmd_pkg_get__catalog_file()
{
    local url=$1
    local file conffile

    for file in /etc/opt/csw/pkg-get.conf /opt/csw/etc/pkg-get.conf /etc/pkg-get.conf; do
        if [[ -f $file ]]; then
            conffile=$file
            break
        fi
    done
    conffile=${conffile:-/opt/csw/etc/pkg-get.conf}

    if [[ ! $url ]]; then
        url=$(_comp_awk -F = '$1 == "url" { print $2 }' "$conffile")
    fi

    REPLY=${url##*//}
    REPLY=${REPLY%%/*}
    REPLY=/var/pkg-get/catalog-$REPLY
}

_comp_cmd_pkg_get()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local url command=""
    if [[ $prev == "-s" ]]; then
        return 1
    fi

    local i=${#words[@]}
    while ((i > 0)); do
        if [[ ${words[--i]} == -s ]]; then
            url=${words[i + 1]}
        fi
        if [[ ${words[i]} == @(-[aDdiUu]|available|describe|download|install|list|updatecatalog|upgrade) ]]; then
            command=${words[i]}
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

    if [[ $cur == -* ]]; then
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
