# bash completion for getent                               -*- shell-script -*-

_comp_cmd_getent()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[s]*)'
    local i db="" has_db=""
    for ((i = 1; i < cword; i++)); do
        # shellcheck disable=SC2254
        case ${words[i]} in
            --version | --usage | --help | -${noargopts}[V?])
                return
                ;;
            --service | -${noargopts}s)
                ((i++))
                ;;
            -*) ;;

            *)
                # First non-option value is the db
                db=${words[i]}
                has_db=set
                break
                ;;
        esac
    done

    case $db in
        passwd)
            _comp_compgen -- -u
            return
            ;;
        group)
            _comp_compgen -- -g
            return
            ;;
        services)
            _comp_compgen -- -s
            return
            ;;
        hosts)
            _comp_compgen -- -A hostname
            return
            ;;
        protocols | networks | ahosts | ahostsv4 | ahostsv6 | rpc)
            _comp_compgen_split -- "$("$1" "$db" | _comp_awk '{ print $1 }')"
            return
            ;;
        aliases | shadow | gshadow)
            _comp_compgen_split -- "$("$1" "$db" | cut -d: -f1)"
            return
            ;;
        ethers | netgroup)
            return
            ;;
    esac

    # shellcheck disable=SC2254
    case $prev in
        -${noargopts}s | --service)
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    elif [[ ! $has_db ]]; then
        _comp_compgen -- -W 'passwd group hosts services protocols networks
            ahosts ahostsv4 ahostsv6 aliases ethers netgroup rpc shadow
            gshadow'
    fi
} &&
    complete -F _comp_cmd_getent getent

# ex: filetype=sh
