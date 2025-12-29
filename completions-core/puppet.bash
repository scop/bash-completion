# bash completion for puppet                               -*- shell-script -*-

_comp_cmd_puppet__logdest()
{
    if [[ ! $cur ]]; then
        _comp_compgen -- -W 'syslog console /'
    else
        _comp_compgen -- -W 'syslog console'
        _comp_compgen -a filedir
    fi
}

_comp_cmd_puppet__digest()
{
    _comp_compgen -- -W 'MD5 MD2 SHA1 SHA256'
}

_comp_cmd_puppet__certs()
{
    local puppetca="puppet cert"
    PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin type puppetca &>/dev/null &&
        puppetca=puppetca

    if [[ $1 == --all ]]; then
        cert_list=$(
            $puppetca --list --all |
                command sed -e 's/^[+-]\{0,1\}[[:space:]]*\([^[:space:]]\{1,\}\)[[:space:]]\{1,\}.*$/\1/'
        )
    else
        cert_list=$("$puppetca" --list)
    fi
    _comp_compgen -a -- -W "$cert_list"
}

_comp_cmd_puppet__types()
{
    puppet_types=$(
        puppet describe --list | command sed -e 's/^\([^[:space:]]\{1,\}\).*$/\1/'
    )
    _comp_compgen -a -- -W "$puppet_types"
}

_comp_cmd_puppet__references()
{
    local puppetdoc="puppet doc"
    PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin type puppetdoc &>/dev/null &&
        puppetdoc=puppetdoc

    puppet_doc_list=$(
        $puppetdoc --list | command sed -e 's/^\([^[:space:]]\{1,\}\).*$/\1/'
    )
    _comp_compgen -a -- -W "$puppet_doc_list"
}

_comp_cmd_puppet__subcmd_opts()
{
    # puppet cmd help is somewhat slow, avoid if possible
    [[ ! $cur || $cur == -* ]] &&
        _comp_compgen -a usage -- help ${2:+"$2"}
}

_comp_cmd_puppet()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local subcommand="" action

    case $prev in
        -h | --help | -V | --version)
            return
            ;;
    esac

    case ${words[0]} in
        puppetmasterd)
            subcommand=master
            ;;
        puppetd)
            subcommand=agent
            ;;
        puppetca)
            subcommand=cert
            ;;
        ralsh)
            subcommand=resource
            ;;
        puppetrun)
            subcommand=kick
            ;;
        puppetqd)
            subcommand=queue
            ;;
        filebucket)
            subcommand=filebucket
            ;;
        puppetdoc)
            subcommand=doc
            ;;
        pi)
            subcommand=describe
            ;;
        puppet)
            case ${words[1]} in
                agent | apply | cert | describe | doc | filebucket | kick | \
                    master | parser | queue | resource)
                    subcommand=${words[1]}
                    ;;
                *.pp | *.rb)
                    subcommand=apply
                    ;;
                *)
                    _comp_compgen -- -W 'agent apply cert describe doc
                        filebucket kick master parser queue resource'
                    return
                    ;;
            esac
            ;;
    esac

    case $subcommand in
        agent)
            case $prev in
                --certname)
                    _comp_compgen_known_hosts -- "$cur"
                    return
                    ;;
                --digest)
                    _comp_cmd_puppet__digest
                    return
                    ;;
                --fqdn)
                    _comp_compgen_known_hosts -- "$cur"
                    return
                    ;;
                -l | --logdest)
                    _comp_cmd_puppet__logdest
                    return
                    ;;
                --masterport)
                    _comp_compgen -- -W '8140'
                    return
                    ;;
                -w | --waitforcert)
                    _comp_compgen -- -W '0 15 30 60 120'
                    return
                    ;;
                *)
                    _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    # _comp_compgen_usage doesn't grok
                    # [-D|--daemonize|--no-daemonize]
                    _comp_compgen -a -- -W '--no-daemonize'
                    return
                    ;;
            esac
            ;;
        apply)
            case $prev in
                --catalog)
                    _comp_compgen -- -W '-'
                    _comp_compgen -a filedir json
                    return
                    ;;
                --execute)
                    return
                    ;;
                -l | --logdest)
                    _comp_cmd_puppet__logdest
                    return
                    ;;
                *)
                    if [[ $cur == -* ]]; then
                        _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    else
                        _comp_compgen_filedir
                    fi
                    return
                    ;;
            esac
            ;;
        cert)
            case $prev in
                --digest)
                    _comp_cmd_puppet__digest
                    return
                    ;;
                *)
                    action=$prev
                    _comp_compgen -- -W '--digest --debug --help --verbose
                         --version'
                    case $action in
                        fingerprint | list | verify | --fingerprint | --list | \
                            --verify)
                            _comp_compgen -a -- -W '--all'
                            _comp_cmd_puppet__certs --all
                            return
                            ;;
                        generate | --generate)
                            _comp_compgen -a known_hosts -- "$cur"
                            return
                            ;;
                        clean | print | revoke | --clean | --print | --revoke)
                            _comp_cmd_puppet__certs --all
                            return
                            ;;
                        sign | --sign)
                            _comp_compgen -a -- -W '--all'
                            _comp_cmd_puppet__certs
                            return
                            ;;
                        *)
                            _comp_compgen -a -- -W 'clean fingerprint generate
                                list print revoke sign verify reinventory'
                            return
                            ;;
                    esac
                    ;;
            esac
            ;;
        describe)
            _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
            if [[ $cur != -* ]]; then
                _comp_cmd_puppet__types
            fi
            return
            ;;
        doc)
            case $prev in
                -o | --outputdir)
                    _comp_compgen_filedir -d
                    return
                    ;;
                -m | --mode)
                    _comp_compgen -- -W 'text trac pdf rdoc'
                    return
                    ;;
                -r | --reference)
                    _comp_cmd_puppet__references
                    return
                    ;;
                *)
                    if [[ $cur == -* ]]; then
                        _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    else
                        _comp_compgen_filedir
                    fi
                    return
                    ;;
            esac
            ;;
        filebucket)
            case $prev in
                -s | --server)
                    _comp_compgen_known_hosts -- "$cur"
                    return
                    ;;
                -b | --bucket)
                    _comp_compgen_filedir -d
                    return
                    ;;
                *)
                    if [[ $cur == -* ]]; then
                        _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    else
                        _comp_compgen -- -W 'backup get restore'
                        _comp_compgen -a filedir
                    fi
                    return
                    ;;
            esac
            ;;
        kick)
            case $prev in
                -c | --class)
                    return
                    ;;
                --host)
                    _comp_compgen_known_hosts -- "$cur"
                    return
                    ;;
                -t | --tag)
                    return
                    ;;
                *)
                    if [[ $cur == -* ]]; then
                        _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    else
                        _comp_compgen_known_hosts -- "$cur"
                    fi
                    return
                    ;;
            esac
            ;;
        master)
            case $prev in
                -l | --logdest)
                    _comp_cmd_puppet__logdest
                    return
                    ;;
                *)
                    _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    # _comp_compgen_usage doesn't grok
                    # [-D|--daemonize|--no-daemonize]
                    _comp_compgen -a -- -W '--no-daemonize'
                    return
                    ;;
            esac
            ;;
        parser)
            action=$prev
            case $action in
                validate)
                    _comp_compgen_filedir pp
                    return
                    ;;
                *)
                    _comp_compgen -- -W 'validate'
                    return
                    ;;
            esac
            ;;
        queue)
            case $prev in
                -l | --logdest)
                    _comp_cmd_puppet__logdest
                    return
                    ;;
                *)
                    if [[ $cur == -* ]]; then
                        _comp_cmd_puppet__subcmd_opts "$1" "$subcommand"
                    else
                        _comp_compgen_filedir
                    fi
                    return
                    ;;
            esac
            ;;
        resource | *)
            _comp_cmd_puppet__subcmd_opts "$1" ${subcommand:+"$subcommand"}
            return
            ;;
    esac
} &&
    complete -F _comp_cmd_puppet puppetmasterd puppetd puppetca ralsh \
        puppetrun puppetqd filebucket puppetdoc puppet

# ex: filetype=sh
