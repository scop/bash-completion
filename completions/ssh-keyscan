# ssh-keyscan(1) completion                                -*- shell-script -*-

_comp_cmd_ssh_keyscan()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    local ipvx

    case $prev in
        -*4*)
            ipvx=-4
            ;;
        -*6*)
            ipvx=-6
            ;;
        -*f)
            _comp_compgen_filedir
            return
            ;;
        -*O)
            case $cur in
                hashalg=*)
                    cur=${cur#*=}
                    _comp_compgen -- -W 'sha1 sha256'
                    ;;
                *=*) ;;
                *)
                    _comp_compgen -- -W 'hashalg='
                    compopt -o nospace
                    ;;
            esac
            return
            ;;
        -*p | -*T)
            return
            ;;
        -*t)
            _comp_delimited , -W "dsa ecdsa ed25519 rsa"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    _comp_compgen_known_hosts ${ipvx-} -- "$cur"
} &&
    complete -F _comp_cmd_ssh_keyscan ssh-keyscan

# ex: filetype=sh
