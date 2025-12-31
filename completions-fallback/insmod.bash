# Linux insmod(8) completion                               -*- shell-script -*-

# Use of this file is deprecated.
# Upstream completion is available in kmod >= 34, use that instead.

_comp_cmd_insmod()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # do filename completion for first argument
    if ((cword == 1)); then
        _comp_compgen_filedir '@(?(k)o?(.[gx]z|.zst))'
    else # do module parameter completion
        _comp_compgen_split -- "$(PATH="$PATH:/sbin" modinfo \
            -p "${words[1]}" 2>/dev/null | cut -d: -f1)"
    fi
} &&
    complete -F _comp_cmd_insmod insmod insmod.static

# ex: filetype=sh
