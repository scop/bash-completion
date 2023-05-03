# bash completion for ncftp                                -*- shell-script -*-

_comp_cmd_ncftp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -u | -p | -P | -j | -F)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi

    if [[ $cword -eq 1 && -f ~/.ncftp/bookmarks ]]; then
        _comp_compgen_split -- "$(command sed -ne \
            's/^\([^,]\{1,\}\),.*$/\1/p' ~/.ncftp/bookmarks)"
    fi

} &&
    complete -F _comp_cmd_ncftp -o default ncftp

# ex: filetype=sh
