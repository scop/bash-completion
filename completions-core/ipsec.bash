# Linux ipsec(8) completion (for FreeS/WAN and strongSwan) -*- shell-script -*-

# Complete ipsec.conf conn entries.
#
# Reads a file from stdin in the ipsec.conf(5) format.
_comp_cmd_ipsec__connections()
{
    local keyword name
    while read -r keyword name; do
        if [[ $keyword == [#]* ]]; then continue; fi
        [[ $keyword == conn && $name != '%default' ]] && COMPREPLY+=("$name")
    done
    ((${#COMPREPLY[@]})) &&
        _comp_compgen -- -W '"${COMPREPLY[@]}"'
}

_comp_cmd_ipsec__freeswan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'auto barf eroute klipsdebug look manual pluto
            ranbits rsasigkey setup showdefaults showhostkey spi spigrp tncfg
            whack'
        return
    fi

    case ${words[1]} in
        auto)
            _comp_compgen -- -W '--asynchronous --up --add --delete --replace
                --down --route --unroute --ready --status --rereadsecrets'
            ;;
        manual)
            _comp_compgen -- -W '--up --down --route --unroute --union'
            ;;
        ranbits)
            _comp_compgen -- -W '--quick --continuous --bytes'
            ;;
        setup)
            _comp_compgen -- -W '--start --stop --restart'
            ;;
        *) ;;

    esac
}

_comp_cmd_ipsec__strongswan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'down irdumm leases listaacerts listacerts listalgs
            listall listcacerts listcainfos listcards listcerts listcrls
            listgroups listocsp listocspcerts listpubkeys openac pki pluto pool
            purgecerts purgecrls purgeike purgeocsp ready reload rereadaacerts
            rereadacerts rereadall rereadcacerts rereadcrls rereadgroups
            rereadocspcerts rereadsecrets restart route scdecrypt scencrypt
            scepclient secrets start starter status statusall stop stroke
            unroute uci up update version whack --confdir --copyright
            --directory --help --version --versioncode'
        return
    fi

    case ${words[1]} in
        down | route | status | statusall | unroute | up)
            local confdir=$(ipsec --confdir)
            _comp_cmd_ipsec__connections <"$confdir/ipsec.conf"
            ;;
        list*)
            _comp_compgen -- -W '--utc'
            ;;
        restart | start)
            _comp_compgen -- -W '--attach-gdb --auto-update --debug --debug-all
                --debug-more --nofork'
            ;;
        pki)
            _comp_compgen -- -W '--gen --issue --keyid --print --pub --req
                --self --signcrl --verify'
            ;;
        pool) ;;

        irdumm)
            _comp_compgen_filedir 'rb'
            ;;
        *) ;;

    esac
}

case "$(ipsec --version 2>/dev/null)" in
    *strongSwan*)
        complete -F _comp_cmd_ipsec__strongswan ipsec
        ;;
    *)
        complete -F _comp_cmd_ipsec__freeswan ipsec
        ;;
esac

# ex: filetype=sh
