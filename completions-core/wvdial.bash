# bash completion for wvdial                               -*- shell-script -*-

_comp_cmd_wvdial()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --config)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    local config i IFS=$'\n'

    case $cur in
        -*)
            _comp_compgen_help
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            ;;
        *)
            # start with global and personal config files
            config="/etc/wvdial.conf"$'\n'"$HOME/.wvdialrc"
            # replace with command line config file if present
            for ((i = 1; i < cword; i++)); do
                if [[ ${words[i]} == "--config" ]]; then
                    config=${words[i + 1]}
                    break
                fi
            done
            # parse config files for sections and
            # remove default section
            _comp_compgen_split -l -X 'Defaults' -- "$(command sed -ne \
                's/^\[Dialer \(.*\)\]$/\1/p' "$config" 2>/dev/null)"
            # escape spaces
            COMPREPLY=("${COMPREPLY[@]// /\\ }")
            ;;
    esac

} &&
    complete -F _comp_cmd_wvdial wvdial

# ex: filetype=sh
