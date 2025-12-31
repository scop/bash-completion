# lzma(1) completion                                       -*- shell-script -*-
# by Per Øyvind Karlsen <peroyvind@mandriva.org>

_comp_cmd_lzma()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '-{1..9}'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local xspec="*.@(lzma|tlz)"

    if [[ $prev == --* ]]; then
        [[ $prev == --@(decompress|list|test) ]] && xspec="!"$xspec
        [[ $prev == --compress ]] && xspec=
    elif [[ $prev == -* ]]; then
        [[ $prev == -*[dt]* ]] && xspec="!"$xspec
        [[ $prev == -*z* ]] && xspec=
    fi

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_lzma lzma

# ex: filetype=sh
