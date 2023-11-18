# querybts completion                                      -*- shell-script -*-

_comp_cmd_querybts()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[Bu]*)'
    # shellcheck disable=SC2254
    case $prev in
        --bts | -${noargopts}B)
            _comp_compgen -- -W 'debian guug kde mandrake help'
            return
            ;;
        --ui | --interface | -${noargopts}u)
            _comp_compgen -- -W "newt text gnome"
            return
            ;;
        --mbox-reader-cmd)
            _comp_compgen_commands
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -- -W 'wnpp boot-floppies kernel bugs.debian.org
            cdimage.debian.org general installation-reports listarchives
            lists.debian.org mirrors nm.debian.org press project qa.debian.org
            release-notes security.debian.org tech-ctte upgrade-reports
            www.debian.org'
        _comp_compgen -ax apt-cache packages
    fi
} &&
    complete -F _comp_cmd_querybts querybts

# ex: filetype=sh
