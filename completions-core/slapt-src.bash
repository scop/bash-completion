# slapt-src(8) completion                                  -*- shell-script -*-

_comp_cmd_slapt_src()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    case "$prev" in
        --config | -c)
            _comp_compgen_filedir
            return
            ;;
        --search | -s | --postprocess | -p)
            # argument required but no completions available
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        if [[ ${COMPREPLY-} ]]; then
            [[ $COMPREPLY == *= ]] && compopt -o nospace
            return
        fi
    fi

    local i t=""
    # search for last action (-i|-w|-b|-f)
    for ((i = ${#words[@]} - 1; i > 0; i--)); do
        if [[ ${words[i]} == -@([iwfb]|-install|-show|-build|-fetch) ]]; then
            t="all"
            break
        fi
    done
    if [[ $t != all ]]; then
        return
    fi

    local config="/etc/slapt-get/slapt-srcrc" # default config location
    # search for config
    for ((i = ${#words[@]} - 1; i > 0; i--)); do
        if [[ ${words[i]} == -@(c|-config) ]]; then
            local REPLY
            _comp_expand_tilde "${words[i + 1]-}"
            config=$REPLY
            break
        fi
        if [[ ${words[i]} == --config=?* ]]; then
            config="${words[i]#*=}"
            break
        fi
    done
    [[ -r $config ]] || return

    if [[ $cur == *:* ]]; then
        local name=${cur%:*}
        _comp_compgen_split -l -- "$(
            LC_ALL=C
            "$1" --config "$config" --search "^$name" 2>/dev/null |
                command sed -ne "/^$cur/{s/^$name:\([^ ]*\) .*$/\1/;p;}"
        )"
    else
        _comp_compgen_split -l -- "$(
            LC_ALL=C
            "$1" --config "$config" --search "^$cur" 2>/dev/null |
                command sed -ne "/^$cur/{s/ .*$//;p;}"
        )"
    fi
} &&
    complete -F _comp_cmd_slapt_src slapt-src

# ex: filetype=sh
