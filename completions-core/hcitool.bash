# bash completion for bluez utils                          -*- shell-script -*-

_comp_cmd_hcitool__bluetooth_addresses()
{
    if [[ ${COMP_BLUETOOTH_SCAN-} ]]; then
        _comp_compgen -a split -- "$(hcitool scan | _comp_awk '/^\t/{print $1}')"
    fi
}

_comp_cmd_hcitool__bluetooth_devices()
{
    _comp_compgen -a split -- "$(hcitool dev | _comp_awk '/^\t/{print $1}')"
}

_comp_cmd_hcitool__bluetooth_services()
{
    _comp_compgen -- -W 'DID SP DUN LAN FAX OPUSH FTP HS HF HFAG SAP NAP
        GN PANU HCRP HID CIP A2SRC A2SNK AVRCT AVRTG UDIUE UDITE SYNCML'
}

_comp_cmd_hcitool__bluetooth_packet_types()
{
    _comp_compgen -- -W 'DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3'
}

_comp_cmd_hcitool()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -i)
            _comp_cmd_hcitool__bluetooth_devices
            return
            ;;
        --role)
            _comp_compgen -- -W 'm s'
            return
            ;;
        --pkt-type)
            _comp_cmd_hcitool__bluetooth_packet_types
            return
            ;;
    esac

    [[ $was_split ]] && return

    local REPLY
    if _comp_get_first_arg; then
        case $REPLY in
            name | info | dc | rssi | lq | afh | auth | key | clkoff | lst)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                fi
                ;;
            cc)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '--role --pkt-type'
                else
                    _comp_count_args
                    if ((REPLY == 2)); then
                        _comp_cmd_hcitool__bluetooth_addresses
                    fi
                fi
                ;;
            sr)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                else
                    _comp_compgen -- -W 'master slave'
                fi
                ;;
            cpt)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                else
                    _comp_cmd_hcitool__bluetooth_packet_types
                fi
                ;;
            tpl | enc | clock)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                else
                    _comp_compgen -- -W '0 1'
                fi
                ;;
        esac
    else
        if [[ $cur == -* ]]; then
            _comp_compgen_help
        else
            _comp_compgen -- -W 'dev inq scan name info spinq epinq cmd con cc
                dc sr cpt rssi lq tpl afh lst auth enc key clkoff clock'
        fi
    fi
} &&
    complete -F _comp_cmd_hcitool hcitool

_comp_cmd_sdptool()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --bdaddr)
            _comp_cmd_hcitool__bluetooth_addresses
            return
            ;;
    esac

    [[ $was_split ]] && return

    local REPLY
    if _comp_get_first_arg; then
        case $REPLY in
            search)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '--bdaddr --tree --raw --xml'
                else
                    _comp_cmd_hcitool__bluetooth_services
                fi
                ;;
            browse | records)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '--tree --raw --xml'
                else
                    _comp_cmd_hcitool__bluetooth_addresses
                fi
                ;;
            add)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '--handle --channel'
                else
                    _comp_cmd_hcitool__bluetooth_services
                fi
                ;;
            get)
                if [[ $cur == -* ]]; then
                    _comp_compgen -- -W '--bdaddr --tree --raw --xml'
                fi
                ;;
        esac
    else
        if [[ $cur == -* ]]; then
            _comp_compgen_help
        else
            _comp_compgen -- -W 'search browse records add del get setattr
                setseq'
        fi
    fi
} &&
    complete -F _comp_cmd_sdptool sdptool

_comp_cmd_l2ping()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -i)
            _comp_cmd_hcitool__bluetooth_devices
            return
            ;;
        -s | -c | -t | -d)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    else
        _comp_cmd_hcitool__bluetooth_addresses
    fi
} &&
    complete -F _comp_cmd_l2ping l2ping

_comp_cmd_rfcomm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -f | --config)
            _comp_compgen_filedir
            return
            ;;
        -i)
            _comp_cmd_hcitool__bluetooth_devices
            _comp_cmd_hcitool__bluetooth_addresses
            return
            ;;
    esac

    local REPLY
    if _comp_get_first_arg; then
        local arg=$REPLY
        _comp_count_args
        local args=$REPLY
        if ((args == 2)); then
            _comp_cmd_hcitool__bluetooth_devices
        else
            case $arg in
                connect | bind)
                    if ((args == 3)); then
                        _comp_cmd_hcitool__bluetooth_addresses
                    fi
                    ;;
            esac
        fi
    else
        if [[ $cur == -* ]]; then
            _comp_compgen_help
        else
            _comp_compgen -- -W 'show connect listen watch bind release'
        fi
    fi
} &&
    complete -F _comp_cmd_rfcomm rfcomm

_comp_cmd_ciptool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -i)
            _comp_cmd_hcitool__bluetooth_devices
            _comp_cmd_hcitool__bluetooth_addresses
            return
            ;;
    esac

    local REPLY
    if _comp_get_first_arg; then
        case $REPLY in
            connect | release | loopback)
                local REPLY
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                fi
                ;;
        esac
    else
        if [[ $cur == -* ]]; then
            _comp_compgen_help
        else
            _comp_compgen -- -W 'show search connect release loopback'
        fi
    fi
} &&
    complete -F _comp_cmd_ciptool ciptool

_comp_cmd_dfutool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -d | --device)
            _comp_cmd_hcitool__bluetooth_devices
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        local REPLY
        _comp_count_args
        case $REPLY in
            1)
                _comp_compgen -- -W 'verify modify upgrade archive'
                ;;
            2)
                _comp_compgen_filedir
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_dfutool dfutool

_comp_cmd_hciconfig()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local REPLY
    if _comp_get_first_arg; then
        case $REPLY in
            putkey | delkey)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_addresses
                fi
                ;;
            lm)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_compgen -- -W 'MASTER SLAVE NONE ACCEPT'
                fi
                ;;
            ptype)
                _comp_count_args
                if ((REPLY == 2)); then
                    _comp_cmd_hcitool__bluetooth_packet_types
                fi
                ;;
        esac
    else
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--help --all'
        else
            _comp_compgen -- -W 'up down reset rstat auth noauth encrypt
                noencrypt secmgr nosecmgr piscan noscan iscan pscan ptype name
                class voice iac inqmode inqdata inqtype inqparams pageparms
                pageto afhmode aclmtu scomtu putkey delkey commands features
                version revision lm'
        fi
    fi
} &&
    complete -F _comp_cmd_hciconfig hciconfig

_comp_cmd_hciattach()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-n -p -t -b -s -l'
    else
        local REPLY
        _comp_count_args
        case $REPLY in
            1)
                _comp_expand_glob COMPREPLY '/dev/tty*' &&
                    _comp_compgen -- -W '"${COMPREPLY[@]}"
                        "${COMPREPLY[@]#/dev/}"'
                ;;
            2)
                _comp_compgen -- -W 'any ericsson digi xircom csr bboxes swave
                    bcsp 0x0105 0x080a 0x0160 0x0002'
                ;;
            3)
                _comp_compgen -- -W '9600 19200 38400 57600 115200 230400
                    460800 921600'
                ;;
            4)
                _comp_compgen -- -W 'flow noflow'
                ;;
            5)
                _comp_cmd_hcitool__bluetooth_addresses
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_hciattach hciattach

# ex: filetype=sh
