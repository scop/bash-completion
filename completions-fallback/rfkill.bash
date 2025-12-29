# bash completion for rfkill                               -*- shell-script -*-

# Use of this file is deprecated on systems with util-linux >= 2.31, which
# ships completion for the rfkill included with it.

_comp_cmd_rfkill()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--version'
    else
        case $cword in
            1)
                _comp_compgen -- -W "help event list block unblock"
                ;;
            2)
                if [[ $prev == block || $prev == unblock ]]; then
                    _comp_compgen_split -- "
                        $("$1" list | _comp_awk -F : '/^[0-9]/ {print $1}')
                        all wifi bluetooth uwb wimax wwan gps"
                fi
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_rfkill rfkill

# ex: filetype=sh
