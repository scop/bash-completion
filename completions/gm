# bash completion for gm(1)                                -*- shell-script -*-

_comp_cmd_gm__commands()
{
    _comp_compgen -a split -- "$("$1" help |
        _comp_awk '/^ +[^ ]+ +- / { print $1 }')"
}

_comp_cmd_gm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_cmd_gm__commands "$1"
        return
    elif [[ $cword -eq 2 && ${words[1]} == time ]]; then
        _comp_cmd_gm__commands "$1"
        return
    fi

    local gmcmd=${words[1]}
    [[ $gmcmd == time ]] && gmcmd=${words[2]}

    case $gmcmd in
        help)
            [[ $prev == help ]] && _comp_cmd_gm__commands "$1"
            return
            ;;
        version)
            return
            ;;
    esac

    # TODO... defer some commands to the imagemagick "gm"less completions etc?
    compopt -o default
} &&
    complete -F _comp_cmd_gm gm

# ex: filetype=sh
