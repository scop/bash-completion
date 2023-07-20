# hash completion                                           -*- shell-script -*-

_comp_cmd_hash()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(*[p]*)'
    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}p)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -c help "$1"
        return
    fi

    _comp_compgen_commands
} &&
    complete -F _comp_cmd_hash hash

# ex: filetype=sh
