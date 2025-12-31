# bash completion for FreeBSD portinstall                  -*- shell-script -*-

_comp_cmd_portinstall()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    [[ $prev == -l || $prev == -L || $prev == -o ]] && return

    local -x portsdir=${PORTSDIR:-/usr/ports}/

    # First try INDEX-5
    local indexfile=$portsdir/INDEX-5
    # Then INDEX if INDEX-5 does not exist or system is not FreeBSD 5.x
    [[ ${OSTYPE%.*} == freebsd5 && -f $indexfile ]] ||
        indexfile=$portsdir/INDEX
    [[ -f $indexfile && -r $indexfile ]] || return

    _comp_compgen_split -l -- "$(_comp_awk -F '|' '
        BEGIN { portsdir = ENVIRON["portsdir"]; len = length(portsdir) }
        { print $1 }
        substr($2, 1, len) == portsdir { print substr($2, len + 1) }
        ' "$indexfile")"

} &&
    complete -F _comp_cmd_portinstall -o dirnames portinstall

# ex: filetype=sh
