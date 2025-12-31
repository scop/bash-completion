# vmstat(8) completion                                     -*- shell-script -*-

_comp_cmd_vmstat()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[cMNnwpS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --partition | -${noargopts}[hVcMNnwp])
            return
            ;;
        --unit | -${noargopts}S)
            [[ $OSTYPE == *linux* ]] &&
                _comp_compgen -- -W 'k K m M'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} ]] ||
            _comp_compgen_usage
    fi
} &&
    complete -F _comp_cmd_vmstat vmstat

# ex: filetype=sh
