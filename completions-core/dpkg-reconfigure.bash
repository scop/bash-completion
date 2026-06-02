# dpkg-reconfigure(1) completion

_comp_cmd_dpkg_reconfigure()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local opt

    local noargopts='!(-*|*[fp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --frontend | -${noargopts}f)
            if _comp_expand_glob opt '/usr/share/perl5/Debconf/FrontEnd/*'; then
                opt=("${opt[@]##*/}")
                opt=("${opt[@]%.pm}")
                _comp_compgen -- -W '"${opt[@]}"'
            fi
            return
            ;;
        --priority | -${noargopts}p)
            _comp_compgen -- -W 'low medium high critical'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--frontend --priority --all --unseen-only --help
            --showold --force --terse'
    else
        _comp_compgen -x dpkg installed_packages
    fi
} &&
    complete -F _comp_cmd_dpkg_reconfigure -o default dpkg-reconfigure
