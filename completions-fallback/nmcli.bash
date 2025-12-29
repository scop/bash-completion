# nmcli completion                                         -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# NetworkManager >= 0.9.8.0, use that instead.

_comp_cmd_nmcli__con_id()
{
    _comp_compgen_split -l -- "$(nmcli con list 2>/dev/null |
        tail -n +2 | _comp_awk -F ' {2,}' '{print $1}')"
}

_comp_cmd_nmcli__con_uuid()
{
    _comp_compgen_split -- "$(nmcli con list 2>/dev/null |
        tail -n +2 | _comp_awk -F ' {2,}' '{print $2}')"
}

_comp_cmd_nmcli__ap_ssid()
{
    _comp_compgen_split -l -- "$(nmcli dev wifi list 2>/dev/null |
        tail -n +2 | _comp_awk -F ' {2,}' '{print $1}')"
}

_comp_cmd_nmcli__ap_bssid()
{
    _comp_compgen_split -- "$(nmcli dev wifi list 2>/dev/null |
        tail -n +2 | _comp_awk -F ' {2,}' '{print $2}')"
}

_comp_cmd_nmcli()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -m | --mode)
            _comp_compgen -- -W 'tabular multiline'
            return
            ;;
        -f | --fields)
            _comp_compgen -- -W 'all common'
            return
            ;;
        -e | --escape)
            _comp_compgen -- -W "yes no"
            return
            ;;
        id)
            _comp_cmd_nmcli__con_id
            return
            ;;
        uuid)
            _comp_cmd_nmcli__con_uuid
            return
            ;;
        iface)
            _comp_compgen_available_interfaces
            return
            ;;
        bssid)
            _comp_cmd_nmcli__ap_bssid
            return
            ;;
        wep-key-type)
            _comp_compgen -- -W "key phrase"
            return
            ;;
    esac

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--terse --pretty --mode --fields --escape
                --version --help'
        else
            _comp_compgen -- -W "nm con dev"
        fi
    else
        local object=${words[1]}
        local command=${words[2]}

        case $object in
            nm)
                case $command in
                    enable)
                        _comp_compgen -- -W "true false"
                        return
                        ;;
                    sleep)
                        _comp_compgen -- -W "true false"
                        return
                        ;;
                    wifi)
                        _comp_compgen -- -W "on off"
                        return
                        ;;
                    wwan)
                        _comp_compgen -- -W "on off"
                        return
                        ;;
                    wimax)
                        _comp_compgen -- -W "on off"
                        return
                        ;;
                esac

                _comp_compgen -- -W 'status permissions enable sleep wifi wwan
                    wimax'
                ;;
            con)
                case $command in
                    list)
                        _comp_compgen -- -W 'id uuid'
                        return
                        ;;
                    up)
                        if [[ $cur == -* ]]; then
                            _comp_compgen -- -W '--nowait --timeout'
                        else
                            _comp_compgen -- -W 'id uuid iface ap nsp'
                        fi
                        return
                        ;;
                    down)
                        _comp_compgen -- -W 'id uuid'
                        return
                        ;;
                    delete)
                        _comp_compgen -- -W 'id uuid'
                        return
                        ;;
                esac

                _comp_compgen -- -W 'list status up down delete'
                ;;
            dev)
                case $command in
                    list)
                        _comp_compgen -- -W 'iface'
                        return
                        ;;
                    disconnect)
                        if [[ $cur == -* ]]; then
                            _comp_compgen -- -W '--nowait --timeout'
                        else
                            _comp_compgen -- -W 'iface'
                        fi
                        return
                        ;;
                    wifi)
                        local subcommand=${words[3]}

                        case $subcommand in
                            list)
                                _comp_compgen -- -W 'iface bssid'
                                return
                                ;;
                            connect)
                                if [[ $cur == -* ]]; then
                                    _comp_compgen -- -W '--private --nowait
                                        --timeout'
                                else
                                    if [[ $prev == "connect" ]]; then
                                        _comp_cmd_nmcli__ap_ssid
                                    else
                                        _comp_compgen -- -W 'password
                                            wep-key-type iface bssid name'
                                    fi
                                fi
                                return
                                ;;
                        esac

                        _comp_compgen -- -W 'list connect'
                        return
                        ;;
                esac

                _comp_compgen -- -W 'status list disconnect wifi'
                ;;
        esac

    fi

} &&
    complete -F _comp_cmd_nmcli nmcli

# ex: filetype=sh
