# bash alias completion                                    -*- shell-script -*-

_comp_cmd_alias()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    case "${words[*]}" in
        *" -p "*)
            return
            ;;
        *[^=])
            _comp_compgen -- -A alias
            ;;
        *=)
            COMPREPLY=("$(alias "${cur%=}" 2>/dev/null | command sed \
                -e 's|^alias '"$cur"'\(.*\)$|\1|')")
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -c help -s "$1"
        ((${#COMPREPLY[*]} != 1)) || compopt +o nospace
    fi
} &&
    complete -F _comp_cmd_alias -o nospace alias

# ex: filetype=sh
