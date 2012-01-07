# curl(1) completion                                       -*- shell-script -*-

_curl()
{
    local cur prev words cword
    _init_completion || return

    case $prev in
        --ciphers|--connect-timeout|-C|--continue-at|-F|--form|--form-string|\
        --ftp-account|--ftp-alternative-to-user|-P|--ftp-port|-H|--header|-h|\
        --help|--hostpubmd5|--keepalive-time|--krb|--limit-rate|--local-port|\
        --mail-from|--mail-rcpt|--max-filesize|--max-redirs|-m|--max-time|\
        --pass|--proto|--proto-redir|--proxy-user|--proxy1.0|-Q|--quote|-r|\
        --range|-X|--request|--retry|--retry-delay|--retry-max-time|\
        --socks5-gssapi-service|-t|--telnet-option|--tftp-blksize|-z|\
        --time-cond|--url|-u|--user|-A|--user-agent|-V|--version|-w|\
        --write-out|--resolve|--tlsuser|--tlspassword)
            return
            ;;
        -K|--config|-b|--cookie|-c|--cookie-jar|-D|--dump-header|--egd-file|\
        --key|--libcurl|-o|--output|--random-file|-T|--upload-file|--trace|\
        --trace-ascii|--netrc-file)
            _filedir
            return
            ;;
        --cacert|-E|--cert)
            _filedir '@(c?(e)rt|cer|pem|der)'
            return
            ;;
        --capath)
            _filedir -d
            return
            ;;
        --cert-type|--key-type)
            COMPREPLY=( $( compgen -W 'DER PEM ENG' -- "$cur" ) )
            return
            ;;
        --crlfile)
            _filedir crl
            return
            ;;
        -d|--data|--data-ascii|--data-binary|--data-urlencode)
            if [[ $cur == \@* ]]; then
                cur=${cur:1}
                _filedir
                COMPREPLY=( "${COMPREPLY[@]/#/@}" )
            fi
            return
            ;;
        --delegation)
            COMPREPLY=( $( compgen -W 'none policy always' -- "$cur" ) )
            return
            ;;
        --engine)
            COMPREPLY=( $( compgen -W 'list' -- "$cur" ) )
            return
            ;;
        --ftp-method)
            COMPREPLY=( $( compgen -W 'multicwd nocwd singlecwd' -- "$cur" ) )
            return
            ;;
        --ftp-ssl-ccc-mode)
            COMPREPLY=( $( compgen -W 'active passive' -- "$cur" ) )
            return
            ;;
        --interface)
            _available_interfaces -a
            return
            ;;
        -x|--proxy|--socks4|--socks4a|--socks5|--socks5-hostname)
            _known_hosts_real
            return
            ;;
        --pubkey)
            _filedir pub
            return
            ;;
        --stderr)
            COMPREPLY=( $( compgen -W '-' -- "$cur" ) )
            _filedir
            return
            ;;
        --tlsauthtype)
            COMPREPLY=( $( compgen -W 'SRP' -- "$cur" ) )
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        COMPREPLY=( $( compgen -W '$( _parse_help "$1" )' -- "$cur" ) )
    fi
} &&
complete -F _curl curl

# ex: ts=4 sw=4 et filetype=sh
