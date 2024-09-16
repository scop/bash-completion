# bash completion for slabtop                              -*- shell-script -*-

_comp_cmd_slabtop()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[ds]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --delay | -${noargopts}[hVd])
            return
            ;;
        --sort | -${noargopts}s)
            _comp_compgen_split -- "$(
                "$1" --help | command sed \
                    -e '/^The following are valid sort criteria/,/^$/!d' \
                    -ne 's/^[[:space:]]\(.\):.*/\1/p'
            )"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi
} &&
    complete -F _comp_cmd_slabtop slabtop

# ex: filetype=sh
