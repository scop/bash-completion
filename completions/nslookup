# bash completion for nslookup                             -*- shell-script -*-

_comp_cmd_nslookup__queryclass()
{
    _comp_compgen -a -- -W 'IN CH HS ANY'
}

_comp_cmd_nslookup__querytype()
{
    # https://en.wikipedia.org/wiki/List_of_DNS_record_types
    # Resource records
    local -a types=(
        A AAAA AFSDB APL CAA CDNSKEY CDS CERT CNAME CSYNC DHCID DLV DNAME
        DNSKEY DS EUI48 EUI64 HINFO HIP IPSECKEY KEY KX LOC MX NAPTR NS NSEC
        NSEC3 NSEC3PARAM OPENPGPKEY PTR RRSIG RP SIG SMIMEA SOA SRV SSHFP TA
        TKEY TLSA TSIG TXT URI ZONEMD SVCB HTTPS
    )
    # Other types/pseudo record types
    types+=(AXFR IXFR OPT)
    # Selected obsolete record types
    types+=(SPF)

    _comp_compgen -a -- -W '"${types[@]}"'
}

_comp_cmd_nslookup()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    case $cur in
        -class=* | -cl=*)
            cur=${cur#*=}
            _comp_cmd_nslookup__queryclass
            return
            ;;
        -querytype=* | -type=* | -q=* | -ty=*)
            cur=${cur#*=}
            _comp_cmd_nslookup__querytype
            return
            ;;
        -?*=*)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-all -class= -debug -nodebug -d2 -nod2 -domain=
            -search -nosearch -port= -querytype= -recurse -norecurse -retry=
            -timeout= -vc -novc -fail -nofail'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local REPLY
    _comp_count_args
    if ((REPLY <= 2)); then
        _comp_compgen_known_hosts -- "$cur"
        [[ $REPLY -eq 1 && $cur == @(|-) ]] && COMPREPLY+=(-)
    fi
} &&
    complete -F _comp_cmd_nslookup nslookup

_comp_cmd_host()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            _comp_cmd_nslookup__queryclass
            return
            ;;
        -t)
            _comp_cmd_nslookup__querytype
            return
            ;;
        -m)
            _comp_compgen -- -W 'trace record usage'
            return
            ;;
        -N | -R | -W)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    local REPLY
    _comp_count_args -a "-*[ctmNRW]"
    if ((REPLY == 1)); then
        _comp_compgen_known_hosts -- "$cur"
    elif ((REPLY == 2)); then
        local ipvx
        [[ ${words[*]} =~ \ -[^\ ]*([46]) ]] && ipvx=-${BASH_REMATCH[1]}
        # shellcheck disable=SC2086
        _comp_compgen_known_hosts ${ipvx-} -- "$cur"
    fi
} &&
    complete -F _comp_cmd_host host

# ex: filetype=sh
