# Debian Linux dselect(8) completion

# Use of this file is deprecated.  Upstream completion is available in
# dpkg >= 1.23.8, use that instead.

_comp_cmd_dselect()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --admindir)
            _comp_compgen_filedir -d
            return
            ;;
        -D | -debug)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen -- -W 'access update select install config remove quit'
    fi

} &&
    complete -F _comp_cmd_dselect dselect
