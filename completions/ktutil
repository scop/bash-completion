# ktutil completion                                        -*- shell-script -*-

_comp_cmd_ktutil__heimdal_principals()
{
    _comp_compgen_split -- "$(kadmin -l dump 2>/dev/null |
        _comp_awk '{print $1}')"
}

_comp_cmd_ktutil__heimdal_realms()
{
    _comp_compgen_split -- "$(kadmin -l dump 2>/dev/null |
        _comp_awk '{print $1}' | _comp_awk -F @ '{print $2}')"
}

_comp_cmd_ktutil__heimdal_encodings()
{
    _comp_compgen -- -W 'des-cbc-mcrc des-cbc-md4 des-cbc-md5 des3-cbc-sha1
        arcfour-hmac-md5 aes128-cts-hmac-sha1-96 aes256-cts-hmac-sha1-96'
}

_comp_cmd_ktutil()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local command commands i options

    case $prev in
        -p | --principal)
            _comp_cmd_ktutil__heimdal_principals
            return
            ;;
        -e | --enctype)
            _comp_cmd_ktutil__heimdal_encodings
            return
            ;;
        -a | --admin-server)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -r | --realm)
            _comp_cmd_ktutil__heimdal_realms
            return
            ;;
        -s | -k | --srvtab | --keytab)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    commands='add change copy get list remove rename purge srvconvert
        srv2keytab srvcreate key2srvtab'

    for ((i = 1; i < cword; i++)); do
        case ${words[i]} in
            -k | --keytab)
                ((i++))
                ;;
            -*) ;;

            *)
                command=${words[i]}
                break
                ;;
        esac
    done

    if [[ $cur == -* ]]; then
        case ${command-} in
            add)
                options='-p --principal -V -e --enctype -w --password -r
                    --random -s --no-salt -h --hex'
                ;;
            change)
                options='-r --realm -a --admin-server -s --server-port'
                ;;
            get)
                options='-p --principal -e --enctype -r --realm -a
                    --admin-server -s server --server-port'
                ;;
            list)
                options='--keys --timestamp'
                ;;
            remove)
                options='-p --principal -V --kvno -e --enctype'
                ;;
            purge)
                options='--age'
                ;;
            srv2keytab | key2srvtab)
                options='-s --srvtab'
                ;;
            *)
                options='-k --keytab -v --verbose --version -v --help'
                ;;
        esac
        _comp_compgen -- -W "$options"
    else
        case ${command-} in
            copy)
                _comp_compgen_filedir
                ;;
            get)
                _comp_cmd_ktutil__heimdal_principals
                ;;
            rename)
                _comp_cmd_ktutil__heimdal_principals
                ;;
            *)
                _comp_compgen -- -W "$commands"
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_ktutil ktutil

# ex: filetype=sh
