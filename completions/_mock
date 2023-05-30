# bash completion for mock                                 -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# mock > 1.1.0, use that instead.

_comp_cmd_mock()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local plugins='tmpfs root_cache yum_cache bind_mount ccache'
    local cfgdir=/etc/mock count=0 i

    for i in "${words[@]}"; do
        ((count == cword)) && break
        if [[ $i == --configdir ]]; then
            cfgdir="${words[count + 1]}"
        elif [[ $i == --configdir=* ]]; then
            cfgdir=${i/*=/}
        fi
        ((count++))
    done

    case $prev in
        -h | --help | --copyin | --copyout | --arch | -D | --define | --with | --without | \
            --uniqueext | --rpmbuild_timeout | --sources | --cwd)
            return
            ;;
        -r | --root)
            _comp_compgen_split -- "$(command ls "$cfgdir")" &&
                COMPREPLY=("${COMPREPLY[@]/%.cfg/}")
            return
            ;;
        --configdir | --resultdir)
            _comp_compgen_filedir -d
            return
            ;;
        --spec)
            _comp_compgen_filedir spec
            return
            ;;
        --target)
            # Case-insensitive BRE to match "compatible archs"
            local regex_header='[cC][oO][mM][pP][aA][tT][iI][bB][lL][eE][[:space:]]\{1,\}[aA][rR][cC][hH][sS]'

            # Yep, compatible archs, not compatible build archs
            # (e.g. ix86 chroot builds in x86_64 mock host)
            # This would actually depend on what the target root
            # can be used to build for...
            _comp_compgen_split -- "$(command rpm --showrc | command sed -ne \
                "s/^[[:space:]]*${regex_header}[[:space:]]*:[[:space:]]*\(.*\)/\1/p")"
            return
            ;;
        --enable-plugin | --disable-plugin)
            _comp_compgen -- -W "$plugins"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir '@(?(no)src.r|s)pm'
    fi
} &&
    complete -F _comp_cmd_mock mock

# ex: filetype=sh
