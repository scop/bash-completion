# iwctl(1) completion                                      -*- shell-script -*-

# Clean and remove all lines that are not a first column of output.
# @param $1 Column offset. Some values use multiple lines, so only keep lines
#                          that start at this offset and not more.
_comp_cmd_iwctl__cleanup_output()
{
    local offset="$1"
    shift
    local remove_colors="s/\x1B\[[0-9;]\+m//g"
    local remove_header_lines="1,4d"
    local remove_line_selector_indication="s/^  > /    /"
    local keep_columns_lines="/^ \{${offset}\}[^ ]/!d"
    local format_lstrip="s/^ *\([^ ]\)/\1/"
    command sed \
        -e "${remove_colors}" \
        -e "${remove_header_lines}" \
        -e "${remove_line_selector_indication}" \
        -e "${keep_columns_lines}" \
        -e "${format_lstrip}" \
        "$@"
}

# Extract first column when it has no spaces
_comp_cmd_iwctl__filter_first_column()
{
    local format_column="s/^\([^ ]\+\)  \+.*/\1/g"
    _comp_cmd_iwctl__cleanup_output \
        2 \
        -e "${format_column}"
}

# Extract SSIDs from 'station list' or 'known-networks list'.
# SSIDs have a maximum of 32 characters, and no leading/trailing spaces.
# @param $1 Column offset. See _comp_cmd_iwctl__cleanup_output.
_comp_cmd_iwctl__filter_list_networks()
{
    local offset="$1"
    shift
    local format_network="s/^\(.\{32\}\)  .*/\1/"
    local format_rstrip="s/\([^ ]\)  *$/\1/g"
    _comp_cmd_iwctl__cleanup_output \
        "${offset}" \
        -e "${format_network}" \
        -e "${format_rstrip}"
}

# List devices for given device mode.
# @param $1 iwctl binary.
# @param $2 device mode.
_comp_cmd_iwctl__list_devices()
{
    local iwctl="$1"
    local device_mode="$2"
    "${iwctl}" "${device_mode}" list | _comp_cmd_iwctl__filter_first_column
}

_comp_cmd_iwctl__doublequote_compreply_if_has_space()
{
    local i
    for i in "${!COMPREPLY[@]}"; do
        COMPREPLY[i]=${COMPREPLY[i]//* */\"${COMPREPLY[i]}\"}
    done
}

_comp_cmd_iwctl()
{
    local cur prev words cword comp_args was_split
    # No split on ':' for "connect-hidden" address.
    _comp_initialize -n ":" -s -- "$@" || return
    local prevprev=${words[cword - 2]}
    local prevprevprev=${words[cword - 3]}

    case $prev in
        --username | --password | --passphrase)
            return
            ;;
    esac

    # 'subcmd' can be either 'list' or the command after the 'device' name.
    local subcword cmd="" has_cmd="" subcmd=""
    for ((subcword = 1; subcword < cword; subcword++)); do
        [[ $subcmd == list ]] && break
        [[ $subcmd ]] && subcmd=${words[subcword]} && break
        [[ $has_cmd ]] && subcmd=${words[subcword]} && break
        [[ ${words[subcword]} != --* &&
            ${words[subcword - 1]} != --@(username|password|passphrase) ]] &&
            cmd=${words[subcword]} has_cmd=set
    done

    if [[ ! $has_cmd ]]; then
        case $cur in
            -*)
                _comp_compgen_split -- \
                    "--username --password --passphrase --dont-ask --help"
                ;;
            *)
                _comp_compgen_split -- \
                    "adapter ad-hoc ap device known-networks wsc station dpp pkex debug"
                ;;
        esac
        return
    fi

    case $cmd in
        adapter)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                show) ;;
                set-property)
                    # No handling of properties completion.
                    ;;
                *)
                    [[ ${prevprev} == set-property ]] && return
                    [[ ${prevprevprev} == set-property ]] && return
                    _comp_compgen_split -- "show set-property"
                    ;;
            esac
            ;;
        ad-hoc)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                start | start_open | stop) ;;
                *)
                    _comp_compgen_split -- "start start_open stop"
                    ;;
            esac
            ;;
        ap)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                start | start-profile | stop | show | scan | get-networks) ;;
                *)
                    _comp_compgen_split -- \
                        "start start-profile stop show scan get-networks"
                    ;;
            esac
            ;;
        device)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                show) ;;
                set-property)
                    # No handling of properties completion.
                    ;;
                *)
                    [[ ${prevprev} == set-property ]] && return
                    [[ ${prevprevprev} == set-property ]] && return
                    _comp_compgen_split -- "show set-property"
                    ;;
            esac
            ;;
        known-networks)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$("$1" "$cmd" list | _comp_cmd_iwctl__filter_list_networks 2)"
                    _comp_compgen -a -- -W "list"
                    _comp_cmd_iwctl__doublequote_compreply_if_has_space
                    ;;
                forget | show) ;;
                set-property)
                    # No handling of properties completion.
                    ;;
                *)
                    [[ ${prevprev} == set-property ]] && return
                    [[ ${prevprevprev} == set-property ]] && return
                    _comp_compgen_split -- "forget show set-property"
                    ;;
            esac
            ;;
        wsc)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                push-button | start-user-pin | start-pin | cancel) ;;
                *)
                    [[ ${prevprev} == start-user-pin ]] && return
                    _comp_compgen_split -- "push-button start-user-pin start-pin cancel"
                    ;;
            esac
            ;;
        station)
            [[ $subcmd == list ]] && return
            # All arguments except $prev and trailing empty argument
            local iwctl_args=("${words[@]::${#words[@]}-2}")
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                connect-hidden)
                    # Quote all completions as it does not keep suggesting the
                    # completion anymore if it was half-provided.
                    # It duplicates the completion and then gets obviously stuck.
                    _comp_compgen_split -l -P '"' -S '"' -- \
                        "$("${iwctl_args[@]}" get-hidden-access-points | _comp_cmd_iwctl__filter_first_column)"
                    ;;
                connect | get-bsses)
                    _comp_compgen_split -l -- \
                        "$("${iwctl_args[@]}" get-networks | _comp_cmd_iwctl__filter_list_networks 6)"
                    _comp_cmd_iwctl__doublequote_compreply_if_has_space
                    ;;
                get-networks | get-hidden-access-points)
                    _comp_compgen_split -- "rssi-dbms rssi-bars"
                    ;;
                disconnect | scan | show) ;;
                rssi-dbms | rssi-bars)
                    # get-networks | get-hidden-access-points rssi-dbms | rssi-bars
                    ;;
                *)
                    [[ ${prevprev} == @(connect|connect-hidden|get-bsses) ]] && return
                    [[ ${prevprevprev} == @(connect|connect-hidden|get-bsses) ]] && return
                    _comp_compgen_split -- \
                        "connect connect-hidden disconnect get-networks get-hidden-access-points scan show get-bsses"
                    ;;
            esac
            ;;
        dpp)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                start-enrollee | start-configurator | stop | show) ;;
                *)
                    _comp_compgen_split -- \
                        "start-enrollee start-configurator stop show"
                    ;;
            esac
            ;;
        pkex)
            [[ $subcmd == list ]] && return
            case $prev in
                "$cmd")
                    _comp_compgen_split -l -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" "$cmd")"
                    _comp_compgen -a -- -W "list"
                    ;;
                enroll | configure)
                    _comp_compgen_split -- "key"
                    ;;
                stop | show) ;;
                key)
                    # enroll|configure key
                    ;;
                *)
                    [[ ${prevprev} == key ]] && return
                    _comp_compgen_split -- "stop show enroll configure"
                    ;;
            esac
            ;;
        debug)
            case $prev in
                "$cmd")
                    _comp_compgen_split -- \
                        "$(_comp_cmd_iwctl__list_devices "$1" station)"
                    ;;
                connect | roam)
                    # Not implemented
                    ;;
                autoconnect)
                    _comp_compgen_split -- "on off"
                    ;;
                on | off)
                    # autoconnect on|off
                    ;;
                *)
                    [[ ${prevprev} == @(connect|roam) ]] && return
                    _comp_compgen_split -- "connect roam get-networks autoconnect"
                    ;;
            esac
            ;;
    esac
} &&
    complete -F _comp_cmd_iwctl iwctl
