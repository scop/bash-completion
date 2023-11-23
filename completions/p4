# Perforce completion                                      -*- shell-script -*-
# by Frank Cusack <frank@google.com>

_comp_cmd_p4()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local p4commands p4filetypes

    # rename isn't really a command
    p4commands="$(p4 help commands 2>/dev/null | _comp_awk 'NF>3 {print $1}')"
    p4filetypes="ctext cxtext ktext kxtext ltext tempobj ubinary \
        uresource uxbinary xbinary xltext xtempobj xtext \
        text binary resource"

    if ((cword == 1)); then
        _comp_compgen -- -W "$p4commands"
    elif ((cword == 2)); then
        case $prev in
            help)
                _comp_compgen -- -W "simple commands environment filetypes
                    jobview revisions usage views $p4commands"
                ;;
            admin)
                _comp_compgen -- -W "checkpoint stop"
                ;;
            *) ;;

        esac
    elif ((cword > 2)); then
        case $prev in
            -t)
                case ${words[cword - 2]} in
                    add | edit | reopen)
                        _comp_compgen -- -W "$p4filetypes"
                        ;;
                    *) ;;

                esac
                ;;
            *) ;;

        esac
    fi

} &&
    complete -F _comp_cmd_p4 -o default p4 g4

# ex: filetype=sh
