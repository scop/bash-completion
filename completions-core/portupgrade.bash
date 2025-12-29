# bash completion for FreeBSD portupgrade                  -*- shell-script -*-

_comp_cmd_portupgrade()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    [[ $prev == -l || $prev == -L || $prev == -o ]] && return

    local pkgdir=${PKG_DBDIR:-/var/db/pkg}/

    _comp_compgen -c "$pkgdir$cur" -- -d
    COMPREPLY=("${COMPREPLY[@]#"$pkgdir"}")
    COMPREPLY=("${COMPREPLY[@]%-*}")

} &&
    complete -F _comp_cmd_portupgrade -o dirnames portupgrade

# ex: filetype=sh
