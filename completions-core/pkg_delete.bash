# bash completion for *BSD package management tools        -*- shell-script -*-

_comp_cmd_pkg_delete()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local pkgdir=${PKG_DBDIR:-/var/db/pkg}/

    [[ $prev == -o || $prev == -p || $prev == -W ]] && return

    _comp_compgen -c "$pkgdir$cur" -- -d
    ((${#COMPREPLY[@]} == 0)) || COMPREPLY=("${COMPREPLY[@]#"$pkgdir"}")

} &&
    complete -F _comp_cmd_pkg_delete -o dirnames \
        pkg_delete pkg_info pkg_deinstall

# ex: filetype=sh
