# desktop-file-validate completion

_comp_cmd_desktop_file_validate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir desktop
} &&
    complete -F _comp_cmd_desktop_file_validate desktop-file-validate
