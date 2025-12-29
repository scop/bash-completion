# postcat(1) completion                                    -*- shell-script -*-

_comp_cmd_postcat()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -c)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    local idx qfile=""
    for idx in "${words[@]}"; do
        [[ $idx == -q ]] && qfile=set && break
    done
    if [[ $qfile ]]; then
        _comp_compgen_split -- "$(mailq 2>/dev/null |
            command sed -e '1d; $d; /^[^0-9A-Z]/d; /^$/d; s/[* !].*$//')"
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_postcat postcat

# ex: filetype=sh
