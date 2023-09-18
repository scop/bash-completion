# bts completion                                           -*- shell-script -*-

# Generate bug numbers from bugs cache in ~/.devscripts_cache/bts
_comp_cmd_bts__compgen_cached_bugs()
{
    [[ -d $HOME/.devscripts_cache/bts ]] || return 1
    local bugs=$(
        find "$HOME/.devscripts_cache/bts" -maxdepth 1 \
            -name "${cur}[0-9]*.html" \
            -printf "%f\n" | cut -d'.' -f1
    )
    _comp_compgen -RU bugs -- -W '$bugs'
}

# Generate APT source packages prefixed with "src:"
_comp_cmd_bts__compgen_src_packages_with_prefix()
{
    local _ppn=${cur:4} # partial package name, after stripping "src:"
    local sources
    _comp_compgen -v sources -c "$_ppn" -x apt-cache sources &&
        _comp_compgen -U sources -- -P "src:" -W '"${sources[@]}"'
}

_comp_cmd_bts()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        show | bugs)
            _comp_compgen -- -W 'release-critical RC from: tag: usertag:'
            _comp_compgen -ai bts cached_bugs
            _comp_compgen -ai bts src_packages_with_prefix
            return
            ;;
        select)
            _comp_compgen -- -W 'package: source: maintainer: submitter:
                severity: status: tag: owner: correspondent: affects: bugs:
                users:  archive:'
            return
            ;;
        status)
            _comp_compgen -- -W 'file: fields: verbose'
            _comp_compgen -ai bts cached_bugs
            return
            ;;
        block | unblock)
            _comp_compgen -- -W 'by with'
            return
            ;;
        severity)
            _comp_compgen -- -W 'wishlist minor normal important serious grave
                critical'
            return
            ;;
        limit)
            _comp_compgen -- -W 'submitter date subject msgid package source
                tag severity owner affects archive'
            return
            ;;
        clone | "done" | reopen | archive | unarchive | retitle | summary | submitter | found | notfound | fixed | notfixed | merge | forcemerge | unmerge | claim | unclaim | forwarded | notforwarded | owner | noowner | subscribe | unsubscribe | reportspam | spamreport | affects | usertag | usertags | reassign | tag | tags)
            _comp_compgen -i bts cached_bugs
            return
            ;;
        package)
            _comp_compgen -x apt-cache packages
            return
            ;;
        cache)
            _comp_compgen -x apt-cache packages
            _comp_compgen -ai bts src_packages_with_prefix
            _comp_compgen -a -- -W 'from: release-critical RC'
            return
            ;;
        cleancache)
            _comp_compgen -x apt-cache packages
            _comp_compgen -ai bts src_packages_with_prefix
            _comp_compgen -a -- -W 'from: tag: usertag: ALL'
            return
            ;;
        user)
            # non-predicible arguments
            return
            ;;
        :)
            # Chances are that "src:<src_package>" is being completed
            # COMP_WORDS would be: "bts cleancache src : <partial_pkg_name>"
            pos=$((COMP_CWORD - 2))
            if [[ $pos -gt 0 && ${COMP_WORDS[pos]} == "src" ]]; then
                _comp_compgen -x apt-cache sources

                return
            fi
            ;;
    esac

    [[ $was_split ]] && return

    _comp_compgen -- -W '--offline --online --no-offline --no-action --cache
        --no-cache --cache-mode --cache-delay --mbox --mailreader --cc-addr
        --use-default-cc --no-use-default-cc --sendmail --mutt --no-mutt
        --smtp-host --smtp-username --smtp-helo --bts-server --force-refresh
        --no-force-refresh --only-new --include-resolved --no-include-resolved
        --no-ack --ack --interactive --force-interactive --no-interactive
        --quiet --no-conf --noconf
        show bugs select status clone done reopen archive unarchive retitle
        summary submitter reassign found notfound fixed notfixed block unblock
        merge forcemerge unmerge tag tags affects user usertag usertags claim
        unclaim severity forwarded notforwarded package limit owner noowner
        subscribe unsubscribe reportspam spamreport cache cleancache version
        help'

} &&
    complete -F _comp_cmd_bts bts

# ex: filetype=sh
