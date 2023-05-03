# htpasswd(1) completion                                   -*- shell-script -*-

_comp_cmd_htpasswd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local i o=0 # $o is index of first non-option argument
    for ((i = 1; i <= cword; i++)); do
        case ${words[i]} in
            -*n*) return ;;
            -*) ;;
            *)
                o=$i
                break
                ;;
        esac
    done

    if ((o == 0 || o == cword)); then
        if [[ $cur == -* ]]; then
            _comp_compgen_help
            return
        fi
        # Password file (first non-option argument)
        _comp_compgen_filedir

    elif ((o == cword - 1)); then
        # Username (second non-option argument)
        _comp_compgen_split -- "$(cut -d: -f1 "${words[o]}" 2>/dev/null)"
    fi
} &&
    complete -F _comp_cmd_htpasswd htpasswd

# ex: filetype=sh
