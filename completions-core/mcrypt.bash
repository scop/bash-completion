# mcrypt(1) completion                                     -*- shell-script -*-
# by Ariel Fermani <the_end@bbs.frc.utn.edu.ar>

_comp_cmd_mcrypt()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -g | --openpgp-z)
            _comp_compgen -- -W '{0..9}'
            return
            ;;
        -o | --keymode)
            _comp_compgen_split -- "$("$1" --list-keymodes 2>/dev/null)"
            return
            ;;
        -m | --mode)
            _comp_compgen_split -- "$("$1" --list 2>/dev/null | cut -d: -f2-)"
            return
            ;;
        -a | --algorithm)
            _comp_compgen_split -- "$("$1" --list 2>/dev/null |
                _comp_awk '{print $1}')"
            return
            ;;
        -h | --hash)
            _comp_compgen_split -- "$("$1" --list-hash 2>/dev/null |
                command sed -e 1d)"
            return
            ;;
        -k | -s | --key | --keysize)
            return
            ;;
        -f | -c | --keyfile | --config)
            _comp_compgen_filedir
            return
            ;;
        --algorithms-directory | --modes-directory)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    elif [[ ${words[0]} == mdecrypt ]]; then
        _comp_compgen_filedir nc
    else
        local i decrypt=""
        for ((i = 1; i < cword; i++)); do
            if [[ ${words[i]} == -@(d|-decrypt) ]]; then
                _comp_compgen_filedir nc
                decrypt=set
                break
            fi
        done
        if [[ ! $decrypt ]]; then
            _comp_compgen_filedir
        fi
    fi
} &&
    complete -F _comp_cmd_mcrypt mcrypt mdecrypt

# ex: filetype=sh
