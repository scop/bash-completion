# bash completion for ifstat(1)                            -*- shell-script -*-

_comp_cmd_ifstat()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[idstx]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --scan | --interval | -${noargopts}[hvV])
            return
            ;;
        -${noargopts}i)
            # TODO comma separated
            _comp_compgen_available_interfaces -a
            return
            ;;
        -${noargopts}d)
            # iproute2: no completion (scan delay)
            # traditional: parse driver
            if ! {
                "$1" --help 2>&1 || :
            } |
                command grep -q -- '-d.*--scan'; then
                _comp_compgen_split -- "$("$1" -v | command sed -e 's/[,.]//g' \
                    -ne 's/^.*drivers://p')"
            fi
            return
            ;;
        --noupdate | -${noargopts}s)
            # iproute2: pass through (skip history update)
            # traditional: hostnames (snmp)
            if ! {
                "$1" --help 2>&1 || :
            } |
                command grep -q -- '-s.*--noupdate'; then
                _comp_compgen_known_hosts -- "$cur"
                return
            fi
            ;;
        -${noargopts}t)
            # iproute2: no completion (interval)
            # traditional: pass through (add timestamp)
            ! {
                "$1" --help 2>&1 || :
            } |
                command grep -q -- '-t.*--interval' || return
            ;;
        --extended | -${noargopts}x)
            # iproute2: parse xstat types
            _comp_compgen_split -- "$("$1" -x nonexistent-xstat 2>&1 |
                _comp_awk 'found { print $1 } /supported xstats:/ { found=1 }')"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
} &&
    complete -F _comp_cmd_ifstat ifstat

# ex: filetype=sh
