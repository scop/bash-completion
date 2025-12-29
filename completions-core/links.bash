# bash completion for links                                -*- shell-script -*-

_comp_cmd_links()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -html-t-text-color | -html-t-link-color)
            _comp_compgen -- -W '{0..15}'
            return
            ;;
        -http.fake-firefox | -html-[gt]-ignore-document-color)
            _comp_compgen -- -W '0 1'
            return
            ;;
        --help | -help | -mode | -display | -source | -dump | -width | -max-connections | \
            -max-connections-to-host | -retries | -receive-timeout | \
            -unrestartable-receive-timeout | -*-size | -*-proxy | \
            -append-text-to-dns-lookups | -ssl.client-cert-passwd | -http.fake-* | \
            -http.extra-header | -ftp.anonymous-passwd | -*-color | -*-gamma | \
            -bfu-aspect | -html-image-scale | -html-margin)
            return
            ;;
        -lookup)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -driver)
            local drivers=$("$1" -driver foo 2>&1 |
                command sed -ne '$!d' -e '/^[a-z0-9, ]\{1,\}$/s/,/ /gp')
            [[ $drivers ]] || drivers='x svgalib fb directfb pmshell atheos'
            _comp_compgen -- -W "$drivers"
            return
            ;;
        -codepage | -bookmarks-codepage | -http-assume-codepage)
            _comp_compgen -x iconv charsets
            return
            ;;
        -download-dir)
            _comp_compgen_filedir -d
            return
            ;;
        -bind-address)
            _comp_compgen_ip_addresses
            return
            ;;
        -bind-address-ipv6)
            _comp_compgen_ip_addresses -6
            return
            ;;
        -async-dns | -download-utime | -aggressive-cache | -only-proxies | \
            -http-bugs.* | -http.do-not-track | -ftp.use-* | -ftp.fast | -ftp.set-iptos | \
            -smb.allow-hyperlinks-to-smb | -save-url-history | -dither-letters | \
            -dither-images | -overwrite-instead-of-scroll | -html-*)
            _comp_compgen -- -W '0 1'
            return
            ;;
        -address-preference | -http.referer)
            _comp_compgen -- -W '{0..4}'
            return
            ;;
        -ssl-certificates | -display-optimize | -gamma-correction)
            _comp_compgen -- -W '{0..2}'
            return
            ;;
        -ssl.client-cert-key)
            _comp_compgen_filedir '@(key|pem)'
            return
            ;;
        -ssl.client-cert-crt)
            _comp_compgen_filedir '@(c?(e)rt|cer|pem|der)'
            return
            ;;
        -bookmarks-file)
            _comp_compgen_filedir html
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -R help
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -W '"${COMPREPLY[@]}"' -X "->"
        return
    fi

    local dir
    for dir in .links .links2; do
        if [[ -r ~/$dir/links.his ]]; then
            _comp_compgen -a split -- "$(cat ~/$dir/links.his)"
            _comp_ltrim_colon_completions "$cur"
        fi
    done
    _comp_compgen -a filedir '@(htm|html)'

} &&
    complete -F _comp_cmd_links links links2

# ex: filetype=sh
