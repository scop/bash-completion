# bash completion for nload(1)                             -*- shell-script -*-

_comp_cmd_nload()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[aiotuU]*)'
    case $prev in
        --help | -${noargopts}[haiot])
            return
            ;;
        -${noargopts}[uU])
            _comp_compgen -- -W 'h b k m g H B K M G'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_available_interfaces
} &&
    complete -F _comp_cmd_nload nload

# ex: filetype=sh
