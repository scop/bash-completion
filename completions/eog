# eog(1) completion                                        -*- shell-script -*-

_comp_cmd_eog()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -'?' | --help | --help-all | --help-gtk)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --help-all
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir '@(ani|avif|?(w)bmp|gif|hei[cf]|ico|j2[ck]|jp[cefgx2]|jpeg|jpg2|jxl|pcx|p[bgp]m|pn[gm]|ras|svg?(z)|tga|tif?(f)|webp|x[bp]m)'
} &&
    complete -F _comp_cmd_eog eog

# ex: filetype=sh
