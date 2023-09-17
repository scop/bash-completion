# munin-node-configure completion                          -*- shell-script -*-

_comp_cmd_munin_node_configure()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --config)
            _comp_compgen_filedir
            return
            ;;
        --servicedir | --libdir)
            _comp_compgen_filedir -d
            return
            ;;
        --snmp)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --snmpversion)
            _comp_compgen -- -W '1 2c 3'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_munin_node_configure munin-node-configure

# ex: filetype=sh
