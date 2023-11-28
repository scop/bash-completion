# bash completion for gphoto2(1)                           -*- shell-script -*-

_comp_cmd_gphoto2()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    case $prev in
        --debug-logfile)
            _comp_compgen_filedir
            return
            ;;
        --hook-script)
            _comp_compgen_filedir
            return
            ;;
        --filename)
            _comp_compgen_filedir
            return
            ;;
        -u | --upload-file)
            _comp_compgen_filedir
            return
            ;;
        --port)
            _comp_compgen_split -- "$("$1" --list-ports 2>/dev/null |
                _comp_awk 'NR>3 { print $1 }')"
            _comp_ltrim_colon_completions "$cur"
            return
            ;;
        --camera)
            _comp_compgen_split -l -- "$("$1" --list-cameras 2>/dev/null |
                _comp_awk -F '"' 'NR>2 { print $2 }')"
            return
            ;;
        --get-config | --set-config | --set-config-index | --set-config-value)
            _comp_compgen_split -- "$("$1" --list-config 2>/dev/null)"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi

} &&
    complete -F _comp_cmd_gphoto2 gphoto2

# ex: filetype=sh
