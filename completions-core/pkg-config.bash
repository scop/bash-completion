# bash completion for pkgconfig                            -*- shell-script -*-

_comp_cmd_pkg_config()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --define-variable | --atleast-version | --atleast-pkgconfig-version | \
            --exact-version | --max-version)
            # argument required but no completions available
            return
            ;;
        --variable)
            local word
            for word in "${words[@]:1}"; do
                if [[ $word != -* ]]; then
                    _comp_compgen_split -- "$(
                        "$1" "$word" --print-variables 2>/dev/null
                    )"
                    break
                fi
            done
            return
            ;;
        -\? | --help | --version | --usage)
            # all other arguments are noop with these
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_split -- "$("$1" --list-all 2>/dev/null |
            _comp_awk '{print $1}')"
        _comp_compgen -a filedir pc
    fi
} &&
    complete -F _comp_cmd_pkg_config pkg-config pkgconf

# ex: filetype=sh
