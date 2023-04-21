# iwconfig completion                                      -*- shell-script -*-

_comp_deprecate_var 2.12 \
    COMP_IWLIST_SCAN BASH_COMPLETION_CMD_IWCONFIG_SCAN

_comp_cmd_iwconfig()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        mode)
            _comp_compgen -- -W 'managed ad-hoc master repeater secondary
                monitor'
            return
            ;;
        essid)
            _comp_compgen -- -W 'on off any'
            if [[ ${BASH_COMPLETION_CMD_IWCONFIG_SCAN-} ]]; then
                _comp_compgen -a split -- "$(iwlist "${words[1]}" scan |
                    _comp_awk -F '\"' '/ESSID/ {print $2}')"
            fi
            return
            ;;
        nwid)
            _comp_compgen -- -W 'on off'
            return
            ;;
        channel)
            _comp_compgen_split -- "$(iwlist "${words[1]}" channel |
                _comp_awk '/^[ \t]*Channel/ {print $2}')"
            return
            ;;

        freq)
            _comp_compgen_split -- "$(iwlist "${words[1]}" channel |
                _comp_awk '/^[ \t]*Channel/ {print $4"G"}')"
            return
            ;;
        ap)
            _comp_compgen -- -W 'on off any'
            if [[ ${BASH_COMPLETION_CMD_IWCONFIG_SCAN-} ]]; then
                _comp_compgen -a split -- "$(iwlist "${words[1]}" scan |
                    _comp_awk -F ': ' '/Address/ {print $2}')"
            fi
            return
            ;;
        rate)
            _comp_compgen -- -W 'auto fixed'
            _comp_compgen -a split -- "$(iwlist "${words[1]}" rate |
                _comp_awk '/^[ \t]*[0-9]/ {print $1"M"}')"
            return
            ;;
        rts | frag)
            _comp_compgen -- -W 'auto fixed off'
            return
            ;;
        key | enc)
            _comp_compgen -- -W 'off on open restricted'
            return
            ;;
        power)
            _comp_compgen -- -W 'period timeout off on'
            return
            ;;
        txpower)
            _comp_compgen -- -W 'off on auto'
            return
            ;;
        retry)
            _comp_compgen -- -W 'limit lifetime'
            return
            ;;
    esac

    if ((cword == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--help --version'
        else
            _comp_compgen_available_interfaces -w
        fi
    else
        _comp_compgen -- -W 'essid nwid mode freq channel sens mode ap nick
            rate rts frag enc key power txpower commit'
    fi

} &&
    complete -F _comp_cmd_iwconfig iwconfig

# ex: filetype=sh
