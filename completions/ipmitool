# bash completion for ipmitool                             -*- shell-script -*-

_comp_cmd_ipmitool__singleline_help()
{
    _comp_compgen_split -- "$("$1" "$2" 2>&1 |
        command sed -ne 's/[,\r]//g' -e 's/^.*[Cc]ommands://p')"
}

_comp_cmd_ipmitool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[hVpUekyPmbtBTl])
            return
            ;;
        -*d)
            local -a files
            _comp_expand_glob files '/dev/ipmi* /dev/ipmi/* /dev/ipmidev/*' &&
                _comp_compgen -- -W '"${files[@]##*([^0-9])}"' -X '![0-9]*'
            return
            ;;
        -*I)
            _comp_compgen_split -- "$("$1" -h 2>&1 |
                command sed -e '/^Interfaces:/,/^[[:space:]]*$/!d' \
                    -ne 's/^[[:space:]]\{1,\}\([^[:space:]]\{1,\}\).*/\1/p')"
            return
            ;;
        -*H)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*[fSO])
            _comp_compgen_filedir
            return
            ;;
        -*C)
            _comp_compgen -- -W '{0..14}'
            return
            ;;
        -*L)
            _comp_compgen -- -W 'CALLBACK USER OPERATOR ADMINISTRATOR'
            return
            ;;
        -*A)
            _comp_compgen -- -W 'NONE PASSWORD MD2 MD5 OEM'
            return
            ;;
        -*o)
            _comp_compgen_split -- "$("$1" -o list 2>&1 |
                _comp_awk '/^[ \t]+/ { print $1 }') list"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi

    # Find out command and subcommand

    local cmds=(raw i2c spd lan chassis power event mc sdr sensor fru gendev
        sel pef sol tsol isol user channel session sunoem kontronoem picmg fwum
        firewall shell exec set hpm ekanalyzer)
    local i c cmd="" has_cmd="" subcmd
    for ((i = 1; i < cword; i++)); do
        [[ $has_cmd ]] && subcmd=${words[i]} && break
        for c in "${cmds[@]}"; do
            [[ ${words[i]} == "$c" ]] && cmd=$c has_cmd=set && break
        done
    done

    if [[ ! $has_cmd ]]; then
        _comp_compgen -- -W '"${cmds[@]}"'
        return
    fi

    # Command/subcommand completions

    case $cmd in

        shell) ;;

        exec)
            _comp_compgen_filedir
            ;;

        chassis | power | kontronoem | fwum)
            _comp_cmd_ipmitool__singleline_help "$1" "$cmd"
            ;;

        lan)
            case $subcmd in
                print | set) ;;

                alert)
                    [[ $prev == alert ]] &&
                        _comp_compgen -- -W 'print set'
                    ;;
                stats)
                    [[ $prev == stats ]] &&
                        _comp_compgen -- -W 'print set'
                    ;;
                *)
                    _comp_compgen -- -W 'print set alert stats'
                    ;;
            esac
            ;;

        sdr)
            case $subcmd in
                get | info | type | list | entity) ;;

                elist)
                    _comp_compgen -- -W 'all full compact event mclog fru
                        generic'
                    ;;
                dump)
                    _comp_compgen_filedir
                    ;;
                fill)
                    case $prev in
                        fill)
                            _comp_compgen -- -W 'sensors file'
                            ;;
                        file)
                            _comp_compgen_filedir
                            ;;
                    esac
                    ;;
                *)
                    _comp_compgen -- -W 'get info type list elist entity dump
                        fill'
                    ;;
            esac
            ;;

        sensor)
            case $subcmd in
                list | get | thresh) ;;

                *)
                    _comp_compgen -- -W 'list get thresh'
                    ;;
            esac
            ;;

        sel)
            case $subcmd in
                info | clear | list | elist | delete) ;;

                add | save | writeraw | readraw)
                    _comp_compgen_filedir
                    ;;
                time)
                    [[ $prev == time ]] &&
                        _comp_compgen -- -W 'get set'
                    ;;
                *)
                    _comp_compgen -- -W 'info clear list elist delete add get
                        save writeraw readraw time'
                    ;;
            esac
            ;;

        user)
            case $subcmd in
                summary | list | disable | enable | priv | test) ;;

                set)
                    [[ $prev == set ]] &&
                        _comp_compgen -- -W 'name password'
                    ;;
                *)
                    _comp_compgen -- -W 'summary list set disable enable priv
                        test'
                    ;;
            esac
            ;;

        set)
            [[ $prev == set ]] &&
                _comp_compgen -- -W 'hostname username password privlvl
                    authtype localaddr targetaddr port csv verbose'
            ;;

    esac
} &&
    complete -F _comp_cmd_ipmitool ipmitool

# ex: filetype=sh
