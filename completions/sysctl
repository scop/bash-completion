# bash completion for sysctl                               -*- shell-script -*-

_comp_cmd_sysctl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[rpf]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --pattern | -${noargopts}[hVr])
            return
            ;;
        --load | -${noargopts}[pf])
            _comp_compgen_filedir conf
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
    else
        local suffix=
        [[ $prev == -w ]] && suffix="="
        _comp_compgen_split -S "$suffix" -- "$(
            PATH="$PATH:/sbin" $1 -N -a 2>/dev/null
        )"
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_sysctl sysctl

# ex: filetype=sh
