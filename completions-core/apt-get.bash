# Debian apt-get(8) completion                             -*- shell-script -*-

# @since 2.12
_comp_xfunc_apt_get_compgen_installed_packages()
{
    if [[ -f /etc/debian_version ]]; then
        # Debian system
        _comp_compgen -x dpkg installed_packages
    else
        # assume RPM based
        _comp_compgen -x rpm installed_packages
    fi
}

_comp_cmd_apt_get()
{
    local cur prev words cword comp_args package
    _comp_initialize -n ':=' -- "$@" || return

    local special="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == @(install|remove|auto?(-)remove|purge|source|build-dep|download|changelog) ]]; then
            special=${words[i]}
            break
        fi
    done

    if [[ $special ]]; then
        case $special in
            remove | auto?(-)remove | purge)
                _comp_xfunc_apt_get_compgen_installed_packages
                ;;
            source)
                # Prefer `apt-cache` in the same dir as command
                local pathcmd
                pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
                _comp_compgen -x apt-cache packages
                _comp_compgen -a split -- "$(apt-cache dumpavail |
                    _comp_awk '$1 == "Source:" { print $2 }' | sort -u)"
                ;;
            install | reinstall)
                if _comp_looks_like_path "$cur"; then
                    _comp_compgen_filedir deb
                    return
                elif [[ $cur == *=* ]]; then
                    package="${cur%%=*}"
                    cur="${cur#*=}"
                    _comp_compgen_split -l -- "$(
                        apt-cache --no-generate madison "$package" 2>/dev/null |
                            while IFS=' |' read -r _ version _; do
                                echo "$version"
                            done
                    )"
                    _comp_ltrim_colon_completions "$cur"
                    return
                fi
                ;;&
            build-dep)
                _comp_compgen_filedir -d
                _comp_looks_like_path "$cur" && return
                ;;&
            *)
                _comp_compgen -ax apt-cache packages
                ;;
        esac
        return
    fi

    local noargopts='!(-*|*[eoct]*)'
    # shellcheck disable=SC2254
    case $prev in
        --error-on | --help | --version | --option | -${noargopts}[ehvo])
            return
            ;;
        --config-file | -${noargopts}c)
            _comp_compgen_filedir
            return
            ;;
        --target-release | --default-release | -${noargopts}t)
            # Prefer `apt-cache` in the same dir as command
            local pathcmd
            pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
            _comp_compgen_split -- "$(apt-cache policy | command sed -ne \
                's/^ *release.*[ ,]o=\(Debian\|Ubuntu\),a=\(\w*\).*/\2/p')"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--no-install-recommends --install-suggests
            --download-only --fix-broken --ignore-missing --fix-missing
            --no-download --quiet --simulate --just-print --dry-run --recon
            --no-act --yes --assume-yes --assume-no --no-show-upgraded
            --verbose-versions --host-architecture --build-profiles --compile
            --build --ignore-hold --with-new-pkgs --no-upgrade --only-upgrade
            --allow-downgrades --allow-remove-essential
            --allow-change-held-packages --force-yes --print-uris --purge
            --reinstall --list-cleanup --target-release --default-release
            --trivial-only --no-remove --auto-remove --autoremove --only-source
            --diff-only --dsc-only --tar-only --arch-only --indep-only
            --allow-unauthenticated --no-allow-insecure-repositories
            --allow-releaseinfo-change --show-progress --with-source --error-on
            --help --version --config-file --option'
    else
        _comp_compgen -- -W 'update upgrade dist-upgrade dselect-upgrade
            install reinstall remove purge source build-dep satisfy check
            download clean autoclean autoremove changelog indextargets'
    fi

} &&
    complete -F _comp_cmd_apt_get apt-get

# ex: filetype=sh
