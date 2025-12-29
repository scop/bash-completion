# idn(1) completion                                        -*- shell-script -*-

_comp_cmd_idn()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[p]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hV])
            return
            ;;
        --profile | -${noargopts}p)
            _comp_compgen -- -W 'Nameprep iSCSI Nodeprep Resourceprep trace
                SASLprep'
            return
            ;;
    esac

    if [[ ! $was_split && $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_idn idn

# ex: filetype=sh
