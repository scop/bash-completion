# bash completion for configure                            -*- shell-script -*-

_comp_deprecate_var 2.12 \
    COMP_CONFIGURE_HINTS BASH_COMPLETION_CMD_CONFIGURE_HINTS

_comp_cmd_configure()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -h | --help | -V | --version | --program-prefix | --program-suffix | \
            --program-transform-name)
            return
            ;;
        --*file)
            _comp_compgen_filedir
            return
            ;;
        --*prefix | --*dir)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $was_split || $cur != -* ]]; then
        _comp_compgen_filedir
        return
    fi

    # if $BASH_COMPLETION_CMD_CONFIGURE_HINTS is not null, then completions of
    # the form --option=SETTING will include 'SETTING' as a contextual hint
    if [[ ${BASH_COMPLETION_CMD_CONFIGURE_HINTS-} ]]; then
        _comp_compgen_split -- "$("$1" --help 2>&1 |
            _comp_awk '/^  --[A-Za-z]/ { print $1; \
            if ($2 ~ /--[A-Za-z]/) print $2 }' | command sed -e 's/[[,].*//g')"
        [[ ${COMPREPLY-} == *=* ]] && compopt -o nospace
    else
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_configure configure

# ex: filetype=sh
