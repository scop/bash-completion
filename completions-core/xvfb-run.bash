# bash completion for xvfb-run                             -*- shell-script -*-

_comp_cmd_xvfb_run()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[npsef]*)'
    local i
    for ((i = 1; i <= cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            _comp_command_offset $i
            return
        fi
        # shellcheck disable=SC2254
        [[ ${words[i]} == -${noargopts}[npsef] ]] && ((i++))
    done

    # shellcheck disable=SC2254
    case $prev in
        --help | --server-num | --xauth-protocol | --server-args | -${noargopts}[hnps])
            return
            ;;
        --error-file | --auth-file | -${noargopts}[ef])
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_xvfb_run xvfb-run

# ex: filetype=sh
