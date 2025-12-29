# look(1) completion                                       -*- shell-script -*-

# Use of this file is deprecated on Linux.  Upstream completion is
# available in util-linux >= 2.23, use that instead.

_comp_cmd_look()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen_split -- "$(look "$cur" 2>/dev/null)"
    fi
} &&
    complete -F _comp_cmd_look -o default look

# ex: filetype=sh
