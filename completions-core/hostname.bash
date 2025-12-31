# hostname(1) completion                                   -*- shell-script -*-

_comp_cmd_hostname()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[F]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV])
            return
            ;;
        --file | -${noargopts}F)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $cur == -* ]] &&
        _comp_compgen_help || _comp_compgen_usage
} &&
    complete -F _comp_cmd_hostname hostname

# ex: filetype=sh
