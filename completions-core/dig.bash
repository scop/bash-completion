# bash completion for dig
#
# dig accepts class, RR type, query name, +options and @server in any order.
# Completion mirrors that: a single command-line scan classifies each token,
# then helpers offer whatever is still missing (or +options / @server / a name
# from ~/.ssh/known_hosts).
#
# IANA registries:
#   RR TYPEs: https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4
#   CLASSes:  https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-2
# Excludes Reserved / Unassigned / Private-use rows. CHAOS is dig's spelling of
# class CH (also accepts lowercase "chaos"); kept as a separate completion word.

# We know ANY is a class, but it's more helpful to add it as rr type, to mimic dig's behavior.
_comp_cmd_dig__iana_dns_classes=(
    CH HS IN
)

_comp_cmd_dig__dns_class_words=(
    "${_comp_cmd_dig__iana_dns_classes[@]}" CHAOS
)

_comp_cmd_dig__iana_rr_types=(
    A A6 AAAA AFSDB AMTRELAY ANY APL ATMA AVC AXFR BRID CAA CDNSKEY CDS CERT CLA
    CNAME CSYNC DHCID DLV DNAME DNSKEY DOA DS DSYNC EID EUI48 EUI64 GID GPOS
    HINFO HIP HHIT HTTPS IPN IPSECKEY ISDN IXFR KEY KX L32 L64 LOC LP MAILA MAILB
    MB MD MF MG MINFO MR MX NAPTR NID NIMLOC NINFO NSEC NSEC3 NSEC3PARAM NS NSAP
    NSAP-PTR NULL NXT NXNAME OPENPGPKEY OPT PTR PX RESINFO RKEY RP RRSIG RT SIG
    SMIMEA SOA SPF SRV SSHFP SVCB TA TALINK TLSA TSIG TXT UINFO UID UNSPEC URI
    WALLET WKS X25 ZONEMD
)

# bind and server CHAOS metadata names returned for class CH/CHAOS + type TXT.
_comp_cmd_dig__chaos_txt_name_list='version.bind hostname.bind authors.bind version.server id.server'

_comp_cmd_dig__is_class_token()
{
    local u=${1^^} x
    for x in "${_comp_cmd_dig__dns_class_words[@]}"; do
        [[ $u == "$x" ]] && return 0
    done
    return 1
}

_comp_cmd_dig__is_rr_type_token()
{
    local u=${1^^} x
    for x in "${_comp_cmd_dig__iana_rr_types[@]}"; do
        [[ $u == "$x" ]] && return 0
    done
    return 1
}

# True if $1 (case-insensitive) is a prefix of any class or RR type mnemonic.
_comp_cmd_dig__class_or_type_prefix()
{
    local p q=${1^^}
    [[ -n $q ]] || return 1
    for p in "${_comp_cmd_dig__dns_class_words[@]}" "${_comp_cmd_dig__iana_rr_types[@]}"; do
        [[ $p == "$q"* ]] && return 0
    done
    return 1
}

# Single pass over words[1 .. cword-1] (every token already committed). Sets:
#   _q_class — uppercase class mnemonic in use ("" if none)
#   _q_type  — uppercase RR type mnemonic in use ("" if none)
#   _q_name  — first bare token that is neither class nor type ("" if none)
#
# Bare tokens are checked as RR type before class so meta-name ANY (which is
# both an IANA class and a meta-type) is treated as a type when written bare,
# matching the common usage `dig example.com ANY`. Explicit `-c ANY` still
# classifies as class.
#
# Skips words[cword] entirely: the user is editing it, even when its current
# value already happens to spell a complete mnemonic (e.g. "A" while heading
# toward "AAAA").
_comp_cmd_dig__scan()
{
    _q_class="" _q_type="" _q_name=""
    local i w u v
    for ((i = 1; i < cword; i++)); do
        w=${words[i]}
        case $w in
            -c)
                ((i + 1 < cword)) || continue
                v=${words[i + 1]^^}
                [[ -z $_q_class ]] && _comp_cmd_dig__is_class_token "$v" \
                    && _q_class=$v
                ((i++))
                continue
                ;;
            -t)
                ((i + 1 < cword)) || continue
                v=${words[i + 1]^^}
                [[ -z $_q_type ]] && _comp_cmd_dig__is_rr_type_token "$v" \
                    && _q_type=$v
                ((i++))
                continue
                ;;
            -* | +* | @* | "")
                continue
                ;;
        esac
        u=${w^^}
        if [[ -z $_q_type ]] && _comp_cmd_dig__is_rr_type_token "$u"; then
            _q_type=$u
        elif [[ -z $_q_class ]] && _comp_cmd_dig__is_class_token "$u"; then
            _q_class=$u
        elif [[ -z $_q_name ]]; then
            _q_name=$w
        fi
    done
}

# Suggest whichever of class / type is still missing (dig allows one of each).
# Returns 1 if cur is a flag/+/@/dotted token or both are already set.
_comp_cmd_dig__bare_class_or_type()
{
    [[ $cur != -* && $cur != +* && $cur != @* ]] || return 1
    [[ $cur == *.* ]] && return 1
    [[ -n $_q_class && -n $_q_type ]] && return 1

    compopt -o nosort 2>/dev/null || true
    if [[ -z $_q_class && -z $_q_type ]]; then
        _comp_compgen -- -W '"${_comp_cmd_dig__dns_class_words[@]}"'
        _comp_compgen -a -- -W '"${_comp_cmd_dig__iana_rr_types[@]}"'
    elif [[ -z $_q_type ]]; then
        _comp_compgen -- -W '"${_comp_cmd_dig__iana_rr_types[@]}"'
    else
        _comp_compgen -- -W '"${_comp_cmd_dig__dns_class_words[@]}"'
    fi
    return 0
}

# CHAOS + TXT (in any order, bare or via -c/-t): suggest BIND metadata names.
_comp_cmd_dig__chaos_txt_names()
{
    [[ $cur != -* && $cur != +* && $cur != @* ]] || return 1
    [[ $_q_class == CH || $_q_class == CHAOS ]] || return 1
    [[ $_q_type == TXT ]] || return 1

    compopt -o nosort 2>/dev/null || true
    _comp_compgen -- -W "$_comp_cmd_dig__chaos_txt_name_list"
    return 0
}

# Append NS-hint targets from $BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE for a probe
# name ($_q_name). Plain-text lines: <pattern> <space-separated server names>
# (no @ prefix; completion adds @). Lines starting with # are ignored.
#
# Longest matching pattern wins ($fqdn == pattern or $fqdn == *.<pattern>; probe
# name from _comp_cmd_dig__scan). Row "*" holds default servers when no pattern
# matches: zone hit lists that row then "*"; otherwise "*" then every target from
# non-* rows (deduped). Trailing dots on probe name or pattern are ignored.
#
# Example:
#   . a.root-servers.net. b.root-servers.net.
#   com a.gtld-servers.net. b.gtld-servers.net.
#   internal.example.com resolver1.internal.example.com 10.0.0.53
#   * 1.1.1.1 8.8.8.8 9.9.9.9 127.0.0.53
#
# Bash cannot discover your resolver portably; maintain this file by hand or from
# resolvectl, scutil, /etc/resolv.conf, etc. to define the * row.

_comp_cmd_dig__ns_hints()
{
    local fqdn=${1%.}
    [[ -z ${BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE-} ]] && return
    [[ -r $BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE ]] || return

    local best_targets="" best_len=0 glob_targets=""
    local -A union_seen=()
    local union_others=""
    local line pattern pattern_n targets _tok
    while IFS= read -r line || [[ -n $line ]]; do
        [[ -z $line || $line == \#* ]] && continue
        read -r pattern targets <<<"$line"
        [[ -z $targets ]] && continue

        if [[ $pattern == '*' ]]; then
            glob_targets=$targets
            continue
        fi

        pattern_n=${pattern%.}

        for _tok in $targets; do
            [[ -z ${union_seen[$_tok]+x} ]] || continue
            union_seen[$_tok]=1
            union_others+="${union_others:+ }${_tok}"
        done

        if [[ -n $fqdn &&
            ($fqdn == "$pattern_n" || $fqdn == *."$pattern_n") ]]; then
            if ((${#pattern_n} > best_len)); then
                best_targets=$targets
                best_len=${#pattern_n}
            fi
        fi
    done <"$BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE"

    if [[ -n $best_targets ]]; then
        _comp_compgen -- -W "$best_targets"
        [[ -n $glob_targets ]] && _comp_compgen -a -- -W "$glob_targets"
        return
    fi

    local second=$union_others
    if [[ -n $glob_targets && -n $union_others ]]; then
        local -A in_glob=()
        local _g filtered=""
        for _g in $glob_targets; do
            in_glob[$_g]=1
        done
        for _tok in $union_others; do
            [[ ${in_glob[$_tok]+x} ]] && continue
            filtered+="${filtered:+ }${_tok}"
        done
        second=$filtered
    fi

    [[ -n $glob_targets ]] && _comp_compgen -- -W "$glob_targets"
    [[ -n $second ]] && _comp_compgen -a -- -W "$second"
}

_comp_cmd_dig()
{
    local cur prev words cword comp_args
    local _q_class _q_type _q_name

    # Exclude = (for +opt=value) and + (so "+short" stays one word) from
    # COMP_WORDBREAKS for this command (cf. mutt.bash).
    _comp_initialize -n '=+' -- "$@" || return

    # Drop bashdefault/default fallback (e.g. inherited from _comp_complete_minimal)
    # so an empty COMPREPLY does not fall back to broad hostname completion.
    compopt +o bashdefault +o default 2>/dev/null || :

    _comp_cmd_dig__scan

    case $prev in
        -b | -p | -x | -y)
            return
            ;;
        -c)
            [[ -n $_q_class ]] && return
            compopt -o nosort 2>/dev/null || true
            _comp_compgen -- -W '"${_comp_cmd_dig__dns_class_words[@]}"'
            return
            ;;
        -f | -k)
            _comp_compgen_filedir
            return
            ;;
        -q)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -t)
            [[ -n $_q_type ]] && return
            compopt -o nosort 2>/dev/null || true
            _comp_compgen -- -W '"${_comp_cmd_dig__iana_rr_types[@]}"'
            return
            ;;
    esac

    case $cur in
        -*)
            _comp_compgen -- -W '-4 -6 -b -c -f -h -k -m -p -q -r -t
                -u -v -x -y'
            return
            ;;
        +*)
            if [[ $cur == +tls-ca=* || $cur == +tls-certfile=* ||
                $cur == +tls-keyfile=* ]]; then
                cur=${cur#*=}
                _comp_compgen_filedir
                return
            fi

            [[ $cur == *=* ]] && return

            # +[no]keyword options sourced from dig -h (BIND 9.21.21)
            _comp_compgen -- -W '
                +aaflag +noaaflag +aaonly +noaaonly
                +additional +noadditional +adflag +noadflag
                +all +noall +answer +noanswer
                +authority +noauthority +badcookie +nobadcookie
                +besteffort +nobesteffort +bufsize +bufsize=
                +cdflag +nocdflag +class +noclass +cmd +nocmd
                +coflag +nocoflag +comments +nocomments
                +cookie +nocookie +crypto +nocrypto
                +defname +nodefname +dns64prefix +nodns64prefix
                +dnssec +nodnssec +domain=
                +edns +noedns +edns= +ednsflags=
                +ednsnegotiation +noednsnegotiation
                +ednsopt= +noednsopt
                +expandaaaa +noexpandaaaa +expire +noexpire
                +fail +nofail +header-only +noheader-only
                +https +nohttps +https= +https-get +nohttps-get
                +http-plain +nohttp-plain +http-plain=
                +http-plain-get +nohttp-plain-get
                +identify +noidentify +idn +noidn
                +ignore +noignore +keepalive +nokeepalive
                +keepopen +nokeepopen +multiline +nomultiline
                +ndots= +nsid +nonsid +nssearch +nonssearch
                +onesoa +noonesoa +opcode +noopcode +opcode=
                +padding= +proxy +noproxy +proxy=
                +proxy-plain +noproxy-plain +proxy-plain=
                +qid= +qr +noqr +question +noquestion
                +raflag +noraflag +rdflag +nordflag
                +recurse +norecurse +retry=
                +rrcomments +norrcomments
                +search +nosearch +short +noshort
                +showallmessages +noshowallmessages
                +showbadcookie +noshowbadcookie
                +showbadvers +noshowbadvers
                +showsearch +noshowsearch
                +showtruncated +noshowtruncated
                +split +nosplit +split= +stats +nostats +subnet=
                +svcparamkeycompat +nosvcparamkeycompat
                +tcflag +notcflag +tcp +notcp +timeout=
                +tls +notls +tls-ca +notls-ca +tls-ca=
                +tls-certfile +notls-certfile +tls-certfile=
                +tls-hostname +notls-hostname +tls-hostname=
                +tls-keyfile +notls-keyfile +tls-keyfile=
                +trace +notrace +tries= +ttlid +nottlid
                +ttlunits +nottlunits
                +unknownformat +nounknownformat
                +vc +novc +yaml +noyaml +zflag +nozflag
                +zoneversion +nozoneversion'
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            return
            ;;
        @*)
            # Resolver @server: NS hints (when BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE is set)
            # otherwise ~/.ssh/known_hosts. Probe name comes from _q_name.
            local server=${cur#@}
            cur=$server

            if [[ -n ${BASH_COMPLETION_CMD_DIG_NS_HINTS_FILE-} ]]; then
                compopt -o nosort 2>/dev/null || true
                _comp_cmd_dig__ns_hints "$_q_name"
            else
                _comp_compgen_known_hosts -- "$cur"
            fi

            ((${#COMPREPLY[@]})) && COMPREPLY=("${COMPREPLY[@]/#/@}")
            cur="@$server"
            return
            ;;
    esac

    # CHAOS + TXT names take priority over generic class/type / hostname lists.
    _comp_cmd_dig__chaos_txt_names && return

    # Bare token: complete the missing class or type, otherwise treat cur as a
    # query name and pull from ~/.ssh/known_hosts (dotted, clearly not a
    # class/type prefix, or both class and type are already set).
    if [[ $cur != -* && $cur != +* && $cur != @* ]]; then
        if [[ $cur == *.* ]]; then
            _comp_compgen_known_hosts -- "$cur"
        elif [[ -n $cur ]] && ! _comp_cmd_dig__class_or_type_prefix "$cur"; then
            _comp_compgen_known_hosts -- "$cur"
        elif [[ -n $_q_class && -n $_q_type ]]; then
            _comp_compgen_known_hosts -- "$cur"
        else
            _comp_cmd_dig__bare_class_or_type || true
        fi
        return
    fi
} &&
    complete -F _comp_cmd_dig dig

# ex: filetype=sh
