# wol(1) completion                                        -*- shell-script -*-

_comp_cmd_wol()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    local noargopts='!(-*|*[pwhif]*)'
    # shellcheck disable=SC2254
    case $prev in
        --version | --help | --port | --passwd | --wait | -${noargopts}[Vpw])
            return
            ;;
        --host | --ipaddr | -${noargopts}[hi])
            # Broadcast addresses
            local PATH=$PATH:/sbin
            _comp_compgen_split -- "$({
                ip -c=never addr show || ip addr show || ifconfig -a
            } 2>/dev/null |
                command sed \
                    -ne 's/.*[[:space:]]Bcast:\([^[:space:]]*\).*/\1/p' \
                    -ne 's/.*inet.*[[:space:]]brd[[:space:]]\([^[:space:]]*\).*/\1/p' \
                    -ne 's/.*[[:space:]]broadcast[[:space:]]\{1,\}\([^[:space:]]*\).*/\1/p')"
            _comp_compgen -a known_hosts -- "$cur"
            return
            ;;
        --file | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_mac_addresses
} &&
    complete -F _comp_cmd_wol wol

# ex: filetype=sh
