# bash completion for vpnc                                 -*- shell-script -*-

_comp_cmd_vpnc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --long-help | --version | --id | --username | --domain | \
            --ifname | --application-version | --local-addr | --local-port | \
            --udp-port | --dpd-idle | --target-network | --ifmtu)
            return
            ;;
        --gateway)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --vendor)
            _comp_compgen -- -W 'cisco netscreen'
            return
            ;;
        --natt-mode)
            _comp_compgen -- -W 'natt none force-natt cisco-udp'
            return
            ;;
        --script | --pid-file | --ca-file)
            _comp_compgen_filedir
            return
            ;;
        --dh)
            _comp_compgen -- -W 'dh1 dh2 dh5'
            return
            ;;
        --pfs)
            _comp_compgen -- -W 'nopfs dh1 dh2 dh5 server'
            return
            ;;
        --ifmode)
            _comp_compgen -- -W 'tun tap'
            return
            ;;
        --debug)
            _comp_compgen -- -W '0 1 2 3 99'
            return
            ;;
        --auth-mode)
            _comp_compgen -- -W 'psk cert hybrid'
            return
            ;;
        --ca-dir)
            _comp_compgen_filedir -d
            return
            ;;
        --password-helper)
            _comp_compgen_commands
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- --long-help
    elif _comp_looks_like_path "$cur"; then
        # explicit filename
        _comp_compgen_filedir conf
    else
        # config name, /etc/vpnc/<name>.conf
        local -a configs
        if _comp_expand_glob configs '/etc/vpnc/*.conf'; then
            configs=("${configs[@]##*/}")
            configs=("${configs[@]%.conf}")
            compopt -o filenames
            _comp_compgen -- -W '"${configs[@]}"'
        fi
    fi
} &&
    complete -F _comp_cmd_vpnc vpnc

# ex: filetype=sh
