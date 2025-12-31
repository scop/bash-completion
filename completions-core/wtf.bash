# wtf completion                                           -*- shell-script -*-
# Raphael Droz, 25/09/2009

_comp_cmd_wtf()
{
    local cur prev words cword comp_args addf
    _comp_initialize -- "$@" || return

    [[ $prev == -f ]] && _comp_compgen_filedir && return
    [[ ${words[*]} == *\ -f* ]] && addf= || addf=-f
    if [[ $cur == -* ]]; then
        COMPREPLY=(${addf:+"$addf"})
        return
    fi

    local db="" has_db=""

    set -- "${words[@]}"
    while (($# > 0)); do
        if [[ $1 == -f ]]; then
            shift
            if (($# > 0)); then
                db=$1
                has_db=set
            fi
            break
        fi
        shift
    done

    if [[ ! $has_db ]]; then
        local f
        for f in "${ACRONYMDB-}" /usr/share/misc/acronyms \
            /usr/share/games/bsdgames/acronyms; do
            [[ -f $f ]] && db="$f" has_db=set && break
        done
        [[ $has_db ]] || return
    fi

    _comp_compgen -c "${cur^^}" split \
        -- "$(cut -f 1 -s "$db"* 2>/dev/null) $addf"
} &&
    complete -F _comp_cmd_wtf wtf

# ex: filetype=sh
