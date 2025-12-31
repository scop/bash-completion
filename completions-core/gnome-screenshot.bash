# gnome-screenshot(1) completion                           -*- shell-script -*-

_comp_cmd_gnome_screenshot()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[def]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --help-* | --version | --delay | --display | -${noargopts}[hd])
            return
            ;;
        --border-effect | -${noargopts}e)
            _comp_compgen -- -W 'shadow border vintage none'
            return
            ;;
        --file | -${noargopts}f)
            _comp_compgen_filedir '@(jp?(e)|pn)g'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_gnome_screenshot gnome-screenshot

# ex: filetype=sh
