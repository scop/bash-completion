# svcadm completion                                        -*- shell-script -*-
#
# Copyright 2006 Yann Rouillard <yann@opencsw.org>

#
# svcadm accept any complete FMRI or abbreviated FMRI
#  - a complete FMRI is svc:/foo/bar/bar/baz
#  - abbreviated FMRI are foo/bar/bar/baz, bar/bar/baz, bar/baz or baz
#
# The goal of this function is to be able to propose all alternatives,
# but to not clutter the interface with all completions, we will only
# cut every completion alternative at the next slash.
#
# For example, if the user types <nothing><tab>, we will propose
# for svc://foo/bar/bar/baz the following completion: foo/, bar/ and baz
# If the user types <b><tab>, we will propose: bar/ and baz
# If the user types <bar/><tab>, we will propose: bar/bar/ and bar/baz
#
# By default, the function proproses only abbreviated completions except if the
# user already began to type svc:. In that case we will propose only the
# complete FMRI beginning with the pattern
#
_comp_cmd_svcadm__fmri()
{
    local cur="$1" prefix="$2"
    local cur_prefix fmri fmri_list=""
    local exact_mode="" pattern

    if [[ $cur == $prefix* ]]; then
        [[ $cur == "$prefix" ]] && cur+="/"
        pattern="$cur*"
        exact_mode=set
    else
        pattern="$prefix*/$cur*"
    fi

    cur_prefix="${cur%"${cur##*/}"}"

    for fmri in $(svcs -H -o FMRI "$pattern" 2>/dev/null); do
        local fmri_part_list fmri_part
        if [[ ! $exact_mode ]]; then
            fmri=${fmri#"$prefix/"}

            # we generate all possibles abbreviations for the FMRI
            # no need to have a generic loop as we will have a finite
            # number of components
            local -a tmp
            if _comp_split -F / tmp "$fmri"; then
                set -- "${tmp[@]}"
                case $# in
                    1) fmri_part_list=" $1" ;;
                    2) fmri_part_list=" $2 $1/$2" ;;
                    3) fmri_part_list=" $3 $2/$3 $1/$2/$3" ;;
                    4) fmri_part_list=" $4 $3/$4 $2/$3/$4 $1/$2/$3/$4" ;;
                esac
            fi
        else
            fmri_part_list="$fmri"
        fi

        # Here we make sure the completions begins with the pattern and
        # we cut them at the first slash
        for fmri_part in $fmri_part_list; do
            [[ $fmri_part == $cur* ]] || continue
            local first_part=${fmri_part#"$cur_prefix"}
            first_part=$cur_prefix${first_part%%/*}
            [[ $first_part != "$fmri_part" ]] && first_part+="/"
            fmri_list+=" $first_part"
        done
    done

    _comp_split COMPREPLY "$fmri_list"

    # here we want to detect if there only one completion proposed and that
    # it ends with a slash. That means the users will still have to complete
    # after, so we gain him one tab keystroke by immediately proposing the
    # next completion alternatives
    local i=${#COMPREPLY[*]}
    if [[ $i -gt 0 && ${COMPREPLY[--i]} == */ ]]; then
        # we have to iterate through the list as we may have duplicate
        while ((i != 0)); do
            [[ ${COMPREPLY[i]} != "${COMPREPLY[i - 1]}" ]] && break
            ((i--))
        done
        if ((i == 0)); then
            _comp_cmd_svcadm__fmri "${COMPREPLY[0]}" "$prefix"
            return
        fi
    fi

    # Work-around bash_completion issue where bash interprets a colon
    # as a separator, borrowed from maven completion code which borrowed
    # it from darcs completion code :)
    local colonprefixes=${cur%"${cur##*:}"}
    local i=${#COMPREPLY[*]}
    while ((i-- > 0)); do
        COMPREPLY[i]=${COMPREPLY[i]#"$colonprefixes"}
    done
}

_comp_cmd_svcadm()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    local command_list="enable disable restart refresh clear mark milestone"
    local command="" i

    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == @(enable|disable|restart|refresh|clear|mark|milestone) ]]; then
            command=${words[i]}
            break
        fi
    done

    if [[ ! $command ]]; then
        if [[ ${cur} == -* ]]; then
            _comp_compgen -- -W "-v"
        else
            _comp_compgen -- -W "$command_list"
        fi
    else
        if [[ ${cur} == -* ]]; then
            case "$command" in
                enable)
                    _comp_compgen -- -W "-r -s -t"
                    ;;
                disable)
                    _comp_compgen -- -W "-s -t"
                    ;;
                mark)
                    _comp_compgen -- -W "-I -t"
                    ;;
                milestone)
                    _comp_compgen -- -W "-d"
                    ;;
            esac
        else
            if [[ $command == "mark" && $prev != @(degraded|maintenance) ]]; then
                _comp_compgen -- -W "degraded maintenance"
            elif [[ $command == "milestone" ]]; then
                _comp_cmd_svcadm__fmri "${cur}" "svc:/milestone"
            else
                _comp_cmd_svcadm__fmri "${cur}" "svc:"
            fi
        fi
    fi
} &&
    complete -F _comp_cmd_svcadm svcadm

# ex: filetype=sh
