# gnokii(1) completion                                     -*- shell-script -*-

_comp_cmd_gnokii__memory_type()
{
    # TODO: reduce the number of choices
    _comp_compgen -- -W "IN OU SM ME MT"
}

_comp_cmd_gnokii()
{
    local cur prev words cword comp_args pprev tprev fprev
    _comp_initialize -- "$@" || return

    case $prev in
        --config)
            _comp_compgen_filedir
            return
            ;;
        --phone)
            local config_file
            for config_file in "$XDG_CONFIG_HOME/gnokii/config" \
                "$HOME/.config/gnokii/config" "$HOME/.gnokiirc" \
                "$XDG_CONFIG_DIRS/gnokii/config" /etc/gnokiirc; do
                [[ -f $config_file ]] && break
            done
            [[ ! -f $config_file ]] && return
            _comp_compgen_split -- "$(command sed -n \
                's/^\[phone_\(.*\)\]/\1/p' "$config_file")"
            return
            ;;
        --help)
            _comp_compgen -- -W 'all monitor sms mms phonebook calendar todo
                dial profile settings wap logo ringtone security file other'
            return
            ;;
        --version | --shell | ping)
            return
            ;;

        # MONITOR
        --monitor)
            _comp_compgen -- -W 'delay once'
            return
            ;;
        --getdisplaystatus | --displayoutput)
            return
            ;;
        --netmonitor)
            _comp_compgen -- -W 'reset off field devel next nr'
            return
            ;;

        # SMS
        --sendsms)
            # (how)TODO ?
            return
            ;;
        --savesms)
            _comp_compgen -- -W '--sender --smsc --smscno --folder --location
                --sent --read --deliver --datetime'
            return
            ;;
        --memory-type | --memory | --getsms | --deletesms | --getmms | --deletemms | \
            --getphonebook | --deletephonebook)
            _comp_cmd_gnokii__memory_type
            return
            ;;
        --getsmsc | --getcalendarnote | --deletecalendarnote | --gettodo | \
            --getspeeddial)
            # TODO: grab a specific entry ID
            return
            ;;
        --setsmsc | --smsreader | --createsmsfolder | --deletealltodos | \
            --showsmsfolderstatus)
            return
            ;;
        --deletesmsfolder | --folder)
            # TODO: folderid
            return
            ;;
        --writephonebook)
            _comp_compgen -- -W '--overwrite --find-free --memory-type
                --location --vcard --ldif'
            return
            ;;
        --writecalendarnote | --writetodo)
            _comp_compgen_filedir vcf
            return
            ;;

        # DIAL
        --setspeeddial | --dialvoice | --senddtmf | --answercall | --hangup)
            # TODO
            return
            ;;
        --divert)
            _comp_compgen -- -W '--op'
            return
            ;;

        # PROFILE
        --getprofile | --setactiveprofile)
            # TODO
            return
            ;;
        --setprofile | --getactiveprofile)
            return
            ;;

        # SETTINGS
        --reset)
            _comp_compgen -- -W 'soft hard'
            return
            ;;
        --setdatetime | --setalarm)
            # TODO
            return
            ;;
        --getdatetime | --getalarm)
            return
            ;;

        # WAP
        --getwapbookmark | --writewapbookmark | --deletewapbookmark | \
            --getwapsetting | --writewapsetting | --activatewapsetting)
            return
            ;;

        # LOGOS
        --sendlogo)
            _comp_compgen -- -W 'caller op picture'
            return
            ;;
        --setlogo | --getlogo)
            _comp_compgen -- -W 'op startup caller dealer text'
            return
            ;;
        --viewlogo)
            # TODO: logofile
            return
            ;;

        --entersecuritycode)
            _comp_compgen -- -W 'PIN PIN2 PUK PUK2 SEC'
            return
            ;;

            # TODO: RINGTONES
    esac

    # second level completion
    if [[ $((cword - 2)) -ge 1 && ${words[cword - 2]} =~ --* ]]; then
        pprev=${words[cword - 2]}
        case $pprev in
            --setspeeddial)
                _comp_cmd_gnokii__memory_type
                return
                ;;
            --getsms | --deletesms | --getmms | --deletemms | --getphonebook | \
                --writetodo | --writecalendarnote)
                # TODO: start number
                return
                ;;
            --gettodo | --getcalendarnote)
                _comp_compgen -- -W '{1..9} end --vCal'
                return
                ;;
            --deletecalendarnote)
                _comp_compgen -- -W '{1..9} end'
                return
                ;;
            --divert)
                _comp_compgen -- -W 'register enable query disable erasure'
                return
                ;;
        esac
    fi

    # third level completion
    if [[ $((cword - 3)) -ge 1 && ${words[cword - 3]} =~ --* ]]; then
        tprev=${words[cword - 3]}
        case $tprev in
            --deletesms | --deletemms)
                _comp_compgen -- -W 'end'
                return
                ;;
            --getphonebook | --writetodo | --writecalendarnote)
                _comp_compgen -- -W '{1..9} end'
                return
                ;;
            --gettodo | --getcalendarnote)
                [[ ${words[cword - 1]} == end ]] &&
                    _comp_compgen -- -W '--vCal'
                return
                ;;
            --divert)
                _comp_compgen -- -W '--type'
                return
                ;;
        esac
    fi

    # fourth level completion
    if [[ $((cword - 4)) -ge 1 && ${words[cword - 4]} =~ --* ]]; then
        fprev=${words[cword - 4]}
        case $fprev in
            --getphonebook)
                _comp_compgen -- -W '--raw --vcard --ldif'
                return
                ;;
            --divert)
                _comp_compgen -- -W 'all busy noans outofreach notavail'
                return
                ;;
        esac
    fi

    local all_cmd
    _comp_compgen -Rv all_cmd help -- --help all

    # these 2 below are allowed in combination with others
    local main_cmd
    _comp_split -l main_cmd "$(printf '%s\n' "${all_cmd[@]}" |
        command sed -e '/--config/d;/--phone/d;s/[][\(){}|^$*+?.]/\\&/g')"
    # don't provide main command completions if one is
    # already on the command line
    local IFS='|'
    local regex_main_cmd="(${main_cmd[*]})($|[^_[:alnum:]])"
    IFS=$' \t\n'
    [[ $COMP_LINE =~ $regex_main_cmd ]] && return

    _comp_compgen -- -W '"${all_cmd[@]}"'
} &&
    complete -F _comp_cmd_gnokii gnokii

# ex: filetype=sh
