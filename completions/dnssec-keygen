# bash completion for dnssec-keygen(8)                     -*- shell-script -*-

_comp_cmd_dnssec_keygen__optarg()
{
    local args=$("$1" -h 2>&1 |
        command sed -e 's/|/ /g' -e 's/(.*//' \
            -ne '/^[[:space:]]*'"$2"'/,/^[[:space:]]*[(-]/p' |
        command sed -e 's/^[[:space:]]*'"$2"'.*://' -e '/^[[:space:]]*-/d')
    _comp_compgen -a -- -W '$args'
}

_comp_cmd_dnssec_keygen()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -[hbEgLpsPARIDSi])
            return
            ;;
        -K)
            _comp_compgen_filedir -d
            return
            ;;
        -[ancdfTtm])
            _comp_cmd_dnssec_keygen__optarg "$1" "$prev"
            return
            ;;
        -r)
            _comp_compgen -c "${cur:-/dev/}" filedir
            return
            ;;
        -v)
            _comp_compgen -- -W '{0..10}'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -R help
        ((${#COMPREPLY[@]})) &&
            _comp_compgen -- -W '"${COMPREPLY[@]%:}"'
        return
    fi
} &&
    complete -F _comp_cmd_dnssec_keygen dnssec-keygen

# ex: filetype=sh
