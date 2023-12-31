# tipc(8) completion                                       -*- shell-script -*-

_comp_cmd_tipc__media()
{
    local optind=$1

    if ((cword == optind)); then
        _comp_compgen -- -W 'media'
        return 0
    elif ((cword == optind + 1)); then
        _comp_compgen -- -W 'udp eth ib'
        return 0
    fi

    return 1
}

_comp_cmd_tipc__bearer()
{
    local optind=$1
    local media="" i

    if _comp_cmd_tipc__media "$optind"; then
        return
    fi

    for ((i = 0; i < cword; i++)); do
        if [[ ${words[i]} == 'media' ]]; then
            media=${words[i + 1]}
        fi
    done

    if ((cword == optind + 2)); then
        case "$media" in
            "udp")
                _comp_compgen -- -W 'name'
                ;;
            "eth" | "ib")
                _comp_compgen -- -W 'device'
                ;;
        esac
    elif ((cword == optind + 3)); then
        case "$media" in
            "udp")
                local names=$(
                    tipc bearer list 2>/dev/null | _comp_awk -F : '/^udp:/ {print $2}'
                )
                _comp_compgen -- -W '$names'
                ;;
            "eth")
                local interfaces=$(command ls /sys/class/net/)
                _comp_compgen -- -W '$interfaces'
                ;;
        esac
    fi
}

_comp_cmd_tipc__link_opts()
{
    _comp_compgen -- -W 'priority tolerance window'
}

_comp_cmd_tipc__link()
{
    local optind=$1
    local filter=$2

    if ((cword == optind)); then
        _comp_compgen -- -W 'link'
    elif ((cword == optind + 1)); then
        # awk drops link state and last trailing :
        local links=$(tipc link list 2>/dev/null |
            _comp_awk '{print substr($1, 0, length($1))}')
        local -a exclude
        [[ $filter == peers ]] && exclude=(-X broadcast-link)
        _comp_compgen -- "${exclude[@]}" -W '$links'
    fi
}

_comp_cmd_tipc()
{
    local cur prev words cword comp_args optind i p
    _comp_initialize -- "$@" || return

    optind=1
    COMPREPLY=()

    # Flags can be placed anywhere in the commandline
    case "$cur" in
        -*)
            _comp_compgen -- -W '-h --help'
            return
            ;;
    esac

    if ((cword == 1)); then
        _comp_compgen -- -W 'bearer link media nametable node socket'
        return
    fi

    case "${words[optind]}" in
        bearer)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'enable disable set get list'
                return
            fi

            case "${words[optind]}" in
                enable)
                    local media="" params
                    ((optind++))

                    if ((cword < optind + 4)); then
                        _comp_cmd_tipc__bearer $optind
                        return
                    fi

                    for ((i = 0; i < cword; i++)); do
                        if [[ ${words[i]} == 'media' ]]; then
                            media=${words[i + 1]}
                        fi
                    done
                    case "$media" in
                        "udp")
                            local -a params=("localip" "localport" "remoteip"
                                "remoteport" "domain" "priority")
                            ;;
                        "eth" | "ib")
                            local -a params=("domain" "priority")
                            ;;
                        *)
                            return
                            ;;
                    esac

                    # If the previous word was a known parameter, we assume a
                    # value for that key. Note that this would break if the
                    # user attempts to use a known key as value.
                    for i in "${params[@]}"; do
                        if [[ $prev == "$i" ]]; then
                            return
                        fi
                    done

                    # In order not to print already used options, we remove them
                    for p in "${words[@]}"; do
                        for i in "${params[@]}"; do
                            if [[ $p == "$i" ]]; then
                                params=("${params[@]/$i/}")
                            fi
                        done
                    done

                    _comp_compgen -- -W '"${params[@]}"' -X ''
                    ;;
                disable)
                    ((optind++))

                    _comp_cmd_tipc__bearer $optind
                    ;;
                get)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 1)); then
                        _comp_cmd_tipc__bearer $((optind + 1))
                    fi
                    ;;
                set)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 2)); then
                        _comp_cmd_tipc__bearer $((optind + 2))
                    fi
                    ;;
            esac
            ;;
        link)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'get set list statistics'
                return
            fi

            case "${words[optind]}" in
                get)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 1)); then
                        _comp_cmd_tipc__link $((optind + 1)) "peers"
                    fi
                    ;;
                set)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 2)); then
                        _comp_cmd_tipc__link $((optind + 2)) "peers"
                    fi
                    ;;
                statistics)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_compgen -- -W 'show reset'
                        return
                    fi

                    case "${words[optind]}" in
                        show | reset)
                            _comp_cmd_tipc__link $((optind + 1))
                            ;;
                    esac
                    ;;
            esac
            ;;
        media)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'get set list'
                return
            fi

            case "${words[optind]}" in
                get)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 1)); then
                        _comp_cmd_tipc__media $((optind + 1))
                    fi
                    ;;
                set)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_cmd_tipc__link_opts
                    elif ((cword >= optind + 2)); then
                        _comp_cmd_tipc__media $((optind + 2))
                    fi
                    ;;
            esac
            ;;
        nametable)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'show'
            fi
            ;;
        node)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'list get set'
                return
            fi

            case "${words[optind]}" in
                get | set)
                    ((optind++))

                    if ((cword == optind)); then
                        _comp_compgen -- -W 'address netid'
                    fi
                    ;;
            esac
            ;;
        socket)
            ((optind++))

            if ((cword == optind)); then
                _comp_compgen -- -W 'list'
            fi
            ;;
    esac
} &&
    complete -F _comp_cmd_tipc tipc

# ex: filetype=sh
