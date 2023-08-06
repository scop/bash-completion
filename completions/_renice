# renice(8) completion                                     -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_renice()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local command=$1 curopt i=0

    # walk back through command line and find last option
    while ((i <= cword && ${#COMPREPLY[@]} == 0)); do
        curopt=${words[cword - i]}
        case "$curopt" in
            -u)
                _comp_compgen_allowed_users
                ;;
            -g)
                _comp_compgen_pgids
                ;;
            -p | "$command")
                _comp_compgen_pids
                ;;
        esac
        ((i++))
    done
} &&
    complete -F _comp_cmd_renice renice

# ex: filetype=sh
