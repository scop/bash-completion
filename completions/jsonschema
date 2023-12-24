# bash completion for jsonschema                           -*- shell-script -*-

_comp_cmd_jsonschema()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --error-format | --validator | -[hFV])
            return
            ;;
        --instance | -i)
            _comp_compgen_filedir json
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    local REPLY
    _comp_count_args -a "-*"
    ((REPLY == 1)) || return
    _comp_compgen_filedir '@(json|schema)'
} &&
    complete -F _comp_cmd_jsonschema jsonschema

# ex: filetype=sh
