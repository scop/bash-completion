# hddtemp(8) completion                                    -*- shell-script -*-

_comp_cmd_hddtemp()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[flupsS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --file | -${noargopts}f)
            _comp_compgen_filedir db
            return
            ;;
        --listen | -${noargopts}l)
            _comp_compgen_ip_addresses
            return
            ;;
        --unit | -${noargopts}u)
            _comp_compgen -- -W 'C F'
            return
            ;;
        --port | --separator | --syslog | --version | --help | -${noargopts}[psSvh?])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a -- -W '--help'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -c "${cur:-/dev/}" filedir
    fi
} &&
    complete -F _comp_cmd_hddtemp hddtemp

# ex: filetype=sh
