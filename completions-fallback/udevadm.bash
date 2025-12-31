# udevadm(8) completion                                    -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# systemd >= 196, use that instead.

_comp_cmd_udevadm()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local i udevcmd="" has_udevcmd=""
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} != -* ]]; then
            udevcmd=${words[i]}
            has_udevcmd=set
            break
        fi
    done

    case $prev in
        --help | --version | --property | --children-max | --timeout | \
            --seq-start | --seq-end | --attr-match | --attr-nomatch | \
            --parent-match | --property-match | --tag-match | \
            --subsystem-match | --subsystem-nomatch | --sysname-match | --path)
            return
            ;;
        --log-priority)
            _comp_compgen -- -W 'err info debug'
            return
            ;;
        --query)
            _comp_compgen -- -W 'name symlink path property all'
            return
            ;;
        --name)
            _comp_compgen -c "${cur:-/dev/}" filedir
            return
            ;;
        --device-id-of-file | --exit-if-exists)
            _comp_compgen_filedir
            return
            ;;
        --action)
            _comp_compgen -- -W 'add change remove'
            return
            ;;
        --type)
            _comp_compgen -- -W 'devices subsystems failed'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ ! $has_udevcmd ]]; then
        case $cur in
            -*)
                _comp_compgen -- -W '--help --version --debug'
                ;;
            *)
                _comp_compgen_split -- "$("$1" --help 2>/dev/null |
                    _comp_awk '/^[ \t]/ { print $1 }')"
                ;;
        esac
        return
    fi

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- ${has_udevcmd:+"$udevcmd"} --help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    fi
} &&
    complete -F _comp_cmd_udevadm udevadm

# ex: filetype=sh
