# ccache(1) completion                                     -*- shell-script -*-

_comp_cmd_ccache()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local i
    for ((i = 1; i <= cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            _comp_command_offset $i
            return
        fi
        [[ ${words[i]} == -*[oFM] ]] && ((i++))
    done

    local noargopts='!(-*|*[FMo]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --max-files | --max-size | -${noargopts}[hVFM])
            return
            ;;
        --set-config | -${noargopts}o)
            if [[ $cur != *=* ]]; then
                _comp_compgen_split -S = -- "$("$1" -p 2>/dev/null |
                    _comp_awk '$3 = "=" { print $2 }')"
                [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            fi
            return
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen_help
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_ccache ccache

# ex: filetype=sh
