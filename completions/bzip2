# bash completion for bzip2                                -*- shell-script -*-

_comp_cmd_bzip2()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[bpn]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | -${noargopts}[bhp])
            return
            ;;
        -${noargopts}n)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        local helpopts
        _comp_compgen -Rv helpopts help
        _comp_compgen -- -W '${helpopts[*]//#/} -{2..9}'
        return
    fi

    local xspec="*.?(t)bz2"

    if [[ $prev == --* ]]; then
        [[ $prev == --@(decompress|list|test) ]] && xspec="!"$xspec
        [[ $prev == --compress ]] && xspec=
    elif [[ $prev == -* ]]; then
        [[ $prev == -*[dt]* ]] && xspec="!"$xspec
        [[ $prev == -*z* ]] && xspec=
    fi

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_bzip2 bzip2 pbzip2 lbzip2

# ex: filetype=sh
