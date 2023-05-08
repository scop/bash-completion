# bash completion for xmms                                 -*- shell-script -*-

_comp_cmd_xmms()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[SRA]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hv])
            return
            ;;
        --toggle-shuffle | --toggle-repeat | --toggle-advance | -${noargopts}[SRA])
            _comp_compgen -- -W 'on off'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen_filedir '@(mp[23]|ogg|wav|pls|m3u|xm|mod|s[3t]m|it|mtm|ult|flac)'
    fi

} &&
    complete -F _comp_cmd_xmms xmms

# ex: filetype=sh
