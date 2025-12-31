# badblocks(8) completion                                  -*- shell-script -*-

_comp_cmd_badblocks()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[bcedpt])
            return
            ;;
        -*[io])
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        # Filter out -w (dangerous) and -X (internal use)
        _comp_compgen -R usage
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -X '-[wX]' -W '"${COMPREPLY[@]}"'
        return
    fi

    _comp_compgen -c "${cur:-/dev/}" filedir
} &&
    complete -F _comp_cmd_badblocks badblocks

# ex: filetype=sh
