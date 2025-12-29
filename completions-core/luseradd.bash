# luseradd(1) and lusermod(1) completion                   -*- shell-script -*-

_comp_cmd_luseradd()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[culPpdksg]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --usage | --gecos | --uid | --login | --plainpassword | --password | \
            --commonname | --givenname | --surname | --roomnumber | --telephonenumber | \
            --homephone | -${noargopts}@([culPp]|[?]*))
            return
            ;;
        --directory | --skeleton | -${noargopts}[dk])
            _comp_compgen_filedir -d
            return
            ;;
        --shell | -${noargopts}s)
            _comp_compgen_shells
            return
            ;;
        --gid | -${noargopts}g)
            _comp_compgen_gids
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    [[ ${1##*/} == luseradd ]] || _comp_compgen -- -u
} &&
    complete -F _comp_cmd_luseradd luseradd lusermod

# ex: filetype=sh
