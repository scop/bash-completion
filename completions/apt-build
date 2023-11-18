# Debian apt-build(1) completion                           -*- shell-script -*-

_comp_cmd_apt_build()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local special="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == @(install|remove|source|info|clean) ]]; then
            special=${words[i]}
            break
        fi
    done

    if [[ $special ]]; then
        case $special in
            install | source | info)
                _comp_compgen -x apt-cache packages
                ;;
            remove)
                _comp_compgen -x dpkg installed_packages
                ;;
        esac
        return
    fi

    case $prev in
        --patch | --build-dir | --repository-dir)
            _comp_compgen_filedir
            return
            ;;
        -h | --help)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--help --show-upgraded -u --build-dir
            --repository-dir --build-only --build-command --reinstall --rebuild
            --remove-builddep --no-wrapper --purge --patch --patch-strip -p
            --yes -y --version -v --no-source'

    else
        _comp_compgen -- -W 'update upgrade install remove source dist-upgrade
            world clean info clean-build update-repository'
    fi

} &&
    complete -F _comp_cmd_apt_build apt-build

# ex: filetype=sh
