# bash completion for ulimit                               -*- shell-script -*-

_comp_cmd_ulimit()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # TODO combined option support (-aH, -Sc etc)

    local mode=
    case $prev in
        -a)
            _comp_compgen -- -W "-S -H"
            return
            ;;
        -[SH]) ;;

        -*)
            mode=$prev
            ;;
    esac

    if [[ ! $mode ]]; then
        local word
        for word in "${words[@]}"; do
            [[ $word == -*a* ]] && return
        done

        if [[ $cur == -* ]]; then
            _comp_compgen_usage -c help -s "$1"
            return
        fi
    fi

    [[ ${mode-} ]] && _comp_compgen -- -W "soft hard unlimited"
} &&
    complete -F _comp_cmd_ulimit ulimit

# ex: filetype=sh
