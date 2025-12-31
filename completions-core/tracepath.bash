# tracepath(8) completion                                  -*- shell-script -*-

_comp_cmd_tracepath()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[lmp])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        return
    fi

    local ipvx
    [[ $1 == *6 ]] && ipvx=-6
    _comp_compgen_known_hosts ${ipvx-} -- "$cur"
} &&
    complete -F _comp_cmd_tracepath tracepath tracepath6

# ex: filetype=sh
