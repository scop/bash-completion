# BitKeeper completion                                     -*- shell-script -*-
# adapted from code by  Bart Trojanowski <bart@jukie.net>

_comp_cmd_bk()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local BKCMDS="$(bk help topics 2>/dev/null |
        _comp_awk '/^  bk/ { print $2 }' | xargs printf '%s ')"

    _comp_compgen -- -W "$BKCMDS"
    _comp_compgen -a filedir

} &&
    complete -F _comp_cmd_bk bk

# ex: filetype=sh
