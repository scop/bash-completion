# xdg-settings completion                                  -*- shell-script -*-

_comp_cmd_xdg_settings()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --list | --manual | --version)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help - <<<"$("$1" --help | tr '{|' '\n')"
        return
    fi

    local REPLY
    _comp_count_args
    if ((REPLY == 1)); then
        _comp_compgen -- -W "get check set"
    elif ((REPLY == 2)); then
        _comp_compgen_split -- "$("$1" --list | _comp_awk '!/^Known/ { print $1 }')"
    fi
} &&
    complete -F _comp_cmd_xdg_settings xdg-settings

# ex: filetype=sh
