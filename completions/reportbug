# bash completion for (Debian) reportbug                   -*- shell-script -*-

_comp_cmd_reportbug()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[CefKHPsoiATjVuQtBS]*)'
    # shellcheck disable=SC2254
    case $prev in
        --class | --header | --pseudo-header | --mirror | --list-cc | \
            --subject | --http_proxy | --proxy | --email | --realname | \
            --smtpuser | --smtppasswd | --replyto | --reply-to | \
            --justification | --package-version | --body | --body-file | \
            --timeout | --max-attachment-size | --envelope-from | \
            -${noargopts}[CHPsjV])
            return
            ;;
        --filename | --include | --mta | --output | --attach | -[fioA])
            _comp_compgen_filedir
            return
            ;;
        --keyid | -${noargopts}K)
            _comp_compgen_split -- "$(
                IFS=:
                gpg --list-keys --with-colons 2>/dev/null |
                    while read -ra row; do
                        [[ ${row[0]} == [ps]ub && ${row[11]} == *s* ]] &&
                            printf '%s\n' "${row[4]}"
                    done
            )"
            return
            ;;
        --tag | --ui | --interface | --type | --bts | --severity | --mode | -${noargopts}[TutBS])
            _comp_compgen_split -- "$("$1" "$prev" help 2>&1 |
                command sed -ne '/^[[:space:]]/p')"
            return
            ;;
        --editor | --mua | --mbox-reader-cmd | -${noargopts}e)
            _comp_compgen_commands
            return
            ;;
        --from-buildd)
            _comp_compgen_split -S "_" -- "$(apt-cache dumpavail |
                _comp_awk -F ' ' '$1 == "Source:" && !uniq[$2]++ { print $2 }')"
            return
            ;;
        --smtphost)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --draftpath)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == -*= ]] && compopt -o nospace
        return
    fi

    _comp_compgen -- -W 'wnpp boot-floppies kernel bugs.debian.org
        cdimage.debian.org general installation-reports listarchives
        lists.debian.org mirrors nm.debian.org press project qa.debian.org
        release-notes security.debian.org tech-ctte upgrade-reports
        www.debian.org'
    _comp_compgen -ax apt-cache packages
    _comp_compgen -a filedir
} &&
    complete -F _comp_cmd_reportbug reportbug

# ex: filetype=sh
