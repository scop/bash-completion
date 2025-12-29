# jps(1) completion                                        -*- shell-script -*-

_comp_cmd_jps()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -J* | -help)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        # Not using _comp_compgen_usage because output has [-help] which does
        # not mean -h, -e, -l, -p...
        _comp_compgen -- -W "-q -m -l -v -V -J -help"
        [[ ${COMPREPLY-} == -J* ]] && compopt -o nospace
    else
        _comp_compgen_known_hosts -- "$cur"
    fi
} &&
    complete -F _comp_cmd_jps jps

# ex: filetype=sh
