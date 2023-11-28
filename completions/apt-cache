# Debian apt-cache(8) completion                           -*- shell-script -*-

# List APT binary packages
# @since 2.12
_comp_xfunc_apt_cache_compgen_packages()
{
    _comp_cmd_apt_cache__compgen_packages apt-cache
}

# List APT binary packages
# @param $1  Name of executable
_comp_cmd_apt_cache__compgen_packages()
{
    _comp_compgen_split -- "$("$1" --no-generate pkgnames "$cur" 2>/dev/null)"
}

# List APT source packages
# @since 2.12
_comp_xfunc_apt_cache_compgen_sources()
{
    _comp_cmd_apt_cache__compgen_sources apt-cache
}

# List APT source packages
# @param $1  Name of executable
_comp_cmd_apt_cache__compgen_sources()
{
    _comp_compgen_split -- "$("$1" dumpavail |
        _comp_awk '$1 == "Source:" { print $2 }' | sort -u)"
}

# List APT binary packages
# @deprecated 2.12
_apt_cache_packages()
{
    local packages
    _comp_compgen -v packages -i apt-cache packages apt-cache &&
        printf '%s\n' "${packages[@]}"
}

# List APT source packages
# @deprecated 2.12
_apt_cache_sources()
{
    local sources
    _comp_compgen -v sources -c "$1" -i apt-cache sources apt-cache &&
        printf '%s\n' "${sources[@]}"
}

# List APT source packages
# @deprecated 2.12
_apt_cache_src_packages()
{
    local sources
    _comp_compgen -v sources -i apt-cache sources apt-cache &&
        printf '%s\n' "${sources[@]}"
}

_comp_cmd_apt_cache()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local special="" ispecial
    if [[ $cur != show ]]; then
        for ((ispecial = 1; ispecial < ${#words[@]}; ispecial++)); do
            if [[ ${words[ispecial]} == @(add|depends|dotty|madison|policy|rdepends|show?(pkg|src|)) ]]; then
                special=${words[ispecial]}
                break
            fi
        done
    fi

    if [[ $special && $ispecial -lt $cword ]]; then
        case $special in
            add)
                _comp_compgen_filedir
                ;;

            showsrc)
                _comp_cmd_apt_cache__compgen_sources "$1"
                ;;

            *)
                _comp_cmd_apt_cache__compgen_packages "$1"
                ;;

        esac
        return
    fi

    local noargopts='!(-*|*[cps]*)'
    # shellcheck disable=SC2254
    case $prev in
        --config-file | --pkg-cache | --src-cache | -${noargopts}[cps])
            _comp_compgen_filedir
            return
            ;;
        --with-source)
            _comp_compgen_filedir '@(deb|dsc|changes)'
            _comp_compgen -a -- -f -o plusdirs -X '!?(*/)@(Sources|Packages)'
            return
            ;;
        search)
            if [[ $cur != -* ]]; then
                return
            fi
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--pkg-cache --src-cache --quiet --important
            --no-pre-depends --no-depends --no-recommends --no-suggests
            --no-conflicts --no-breaks --no-replaces --no-enhances --implicit
            --full --all-versions --no-all-versions --generate --no-generate
            --names-only --all-names --recurse --installed --with-source
            --help --version --config-file --option'
    elif [[ ! $special ]]; then
        _comp_compgen -- -W 'gencaches showpkg stats showsrc dump dumpavail
            unmet show search depends rdepends pkgnames dotty xvcg policy
            madison'
    fi

} &&
    complete -F _comp_cmd_apt_cache apt-cache

# ex: filetype=sh
