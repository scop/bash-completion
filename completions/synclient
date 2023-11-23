# bash completion for synclient(1)                         -*- shell-script -*-

_comp_cmd_synclient()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    case $prev in
        -\? | -h | -V)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    elif [[ $cur != *=?* ]]; then
        _comp_compgen_split -S = -- "$("$1" -l 2>/dev/null |
            _comp_awk '/^[ \t]/ { print $1 }')"
        compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_synclient synclient

# ex: filetype=sh
