# pkgadd completion                                        -*- shell-script -*-
#
# Copyright 2006 Yann Rouillard <yann@opencsw.org>

_comp_cmd_pkgadd()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    # if a device directory was given
    # we must complete with the package
    # available in this directory
    local device=/var/spool/pkg
    local i=$cword
    while ((i-- > 0)); do
        case "${words[i]}" in
            -d)
                device="${words[i + 1]}"
                break
                ;;
        esac
    done

    case $prev in
        -d)
            _comp_compgen_filedir pkg
            ;;
        -a | -r | -V)
            _comp_compgen_filedir
            ;;
        -k | -s | -R)
            _comp_compgen_filedir -d
            ;;
        -P | -x) ;;

        *)
            if [[ ${cur} == -* ]]; then
                local -a opts=(-a -A -d -k -n -M -P -r -R -s -v -V -x)
                _comp_compgen -- -W '"${opts[@]}"'
            else
                local -a pkginst_list
                if [[ -d $device ]]; then
                    if _comp_expand_glob pkginst_list '"$device"/*/pkginfo'; then
                        pkginst_list=("${pkginst_list[@]#"$device/"}")
                        pkginst_list=("${pkginst_list[@]%/pkginfo}")
                    fi
                else
                    local REPLY
                    _comp_dequote "$device"
                    _comp_split -l pkginst_list "$(strings "${REPLY-}" |
                        command sed -n 's/^PKG=//p' | sort -u)"
                fi
                ((${#pkginst_list[@]})) &&
                    _comp_compgen -- -W '"${pkginst_list[@]}"'
            fi
            ;;
    esac
} &&
    complete -F _comp_cmd_pkgadd pkgadd

# ex: filetype=sh
