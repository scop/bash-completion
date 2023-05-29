# appdata-validate(1) completion                           -*- shell-script -*-

_comp_cmd_appdata_validate()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -h | --help | --version)
            return
            ;;
        --output-format)
            _comp_compgen_split -- "$("$1" --help | command sed -ne \
                's/--output-format.*\[\(.*\)\]/\1/' -e 's/|/ /gp')"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir appdata.xml
} &&
    complete -F _comp_cmd_appdata_validate appdata-validate

# ex: filetype=sh
