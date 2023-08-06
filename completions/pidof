# pidof(8) completion                                      -*- shell-script -*-

_comp_cmd_pidof()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[o]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | -V | --version | -${noargopts}[hV]*)
            return
            ;;
        --omit-pid | -${noargopts}o)
            _comp_compgen_pids
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_pnames
} &&
    complete -F _comp_cmd_pidof pidof

# ex: filetype=sh
