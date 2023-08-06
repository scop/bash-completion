# newgrp(1) completion                                     -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_newgrp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == "-" ]]; then
        COMPREPLY=(-)
    else
        _comp_compgen_allowed_groups
    fi
} &&
    complete -F _comp_cmd_newgrp newgrp

# ex: filetype=sh
