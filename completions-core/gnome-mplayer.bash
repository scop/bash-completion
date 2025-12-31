# gnome-mplayer(1) completion                              -*- shell-script -*-

_comp_cmd_gnome_mplayer()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -'?' | --help | --help-all | --help-gtk)
            return
            ;;
        --showcontrols | --showsubtitles | --autostart)
            _comp_compgen -- -W '0 1'
            return
            ;;
        --subtitle)
            _comp_compgen_filedir '@(srt|sub|txt|utf|rar|mpsub|smi|js|ssa|ass)'
            return
            ;;
        --tvdriver)
            _comp_compgen -- -W 'v4l v4l2'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_gnome_mplayer gnome-mplayer

# ex: filetype=sh
