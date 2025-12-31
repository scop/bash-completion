# cfagent completion                                       -*- shell-script -*-

_comp_cmd_cfagent()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -f | --file)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_cfagent cfagent

# ex: filetype=sh
