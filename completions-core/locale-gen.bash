# locale-gen(8) completion                                 -*- shell-script -*-

_comp_cmd_locale_gen()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --help | -h)
            return
            ;;
        --aliases)
            _comp_compgen_filedir alias
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_split -- "$(
        _comp_awk '{ print $1 }' /usr/share/i18n/SUPPORTED 2>/dev/null
    )"
} &&
    complete -F _comp_cmd_locale_gen locale-gen

# ex: filetype=sh
