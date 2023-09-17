# lftp(1) completion                                       -*- shell-script -*-

_comp_cmd_lftp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[fceups]*)'
    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
        --help | --version | -${noargopts}[chveups])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_split -- "$("$1" -c "bookmark list" 2>/dev/null)"
    _comp_compgen -a known_hosts -- "$cur"
} &&
    complete -F _comp_cmd_lftp lftp

# ex: filetype=sh
