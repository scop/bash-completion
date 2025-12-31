# scrub(1) completion                                      -*- shell-script -*-

_comp_cmd_scrub()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[bsDpX]*)'
    # shellcheck disable=SC2254
    case $prev in
        --version | --help | --blocksize | --device-size | --dirent | \
            -${noargopts}[vhbsD])
            return
            ;;
        --pattern | -${noargopts}p)
            _comp_compgen_split -- "$("$1" --help 2>&1 |
                _comp_awk '/^Available/{flag=1;next}/^ /&&flag{print $1}')"
            return
            ;;
        --freespace | -${noargopts}X)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_scrub scrub

# ex: filetype=sh
