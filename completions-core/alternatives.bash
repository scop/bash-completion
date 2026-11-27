# bash completion for alternatives

_comp_cmd_alternatives__installed()
{
    local i admindir=${1-}
    if (($# == 0)); then
        for i in alternatives rpm/alternatives; do
            [[ -d /var/lib/$i ]] && admindir=/var/lib/$i && break
        done
    fi
    [[ -d $admindir ]] && _comp_compgen -C "$admindir" -- -fX '*/*'
}

_comp_cmd_alternatives()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local option="" args=0 i
    # Keep an omitted directory distinct from an explicitly empty one.
    local -a REPLY=() dirs=()
    # Each option consumes its own operands.  In particular, an operand that
    # looks like an option must not change the option or the admin directory.
    for ((i = 1; i < cword; i++)); do
        if ((args)); then
            if [[ $option == --admindir ]]; then
                _comp_dequote "${words[i]}" || :
                dirs=("${REPLY[0]-}")
            fi
            ((args--))
            continue
        fi
        option=${words[i]}
        case $option in
            --add-follower | --add-slave) args=5 ;;
            --install) args=4 ;;
            --follower | --slave | \
                --remove-follower | --remove-slave) args=3 ;;
            --remove | --set) args=2 ;;
            --auto | --display | --config | --remove-all | \
                --altdir | --admindir | --family | --initscript) args=1 ;;
        esac
    done

    case $option in
        --help | --usage | --version)
            return
            ;;
    esac

    if ((! args)); then
        _comp_compgen_help - <<<"$(LANG=C "$1" --help 2>&1 | command sed '
            /usage:/,/^[[:space:]]*$/{
              s/^\([[:space:]]*usage:\)\{0,1\}[[:space:]]*[^[:space:]]*alternatives /  /
              s/^[[:space:]]*\[\(-.*\)\]/  \1/
            }
            /common options:/,$s/ --/\n --/g')"
        return
    fi

    case $option in
        --altdir | --admindir)
            _comp_compgen_filedir -d
            ;;
        --install)
            case $args in
                4 | 2) _comp_compgen_filedir ;;
                3) _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"} ;;
                1) ;; # priority
            esac
            ;;
        --follower | --slave)
            case $args in
                3 | 1) _comp_compgen_filedir ;;
                2) _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"} ;;
            esac
            ;;
        --remove | --set)
            case $args in
                2) _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"} ;;
                1) _comp_compgen_filedir ;;
            esac
            ;;
        --auto | --remove-all | --display | --config)
            _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"}
            ;;
        --add-follower | --add-slave)
            case $args in
                5 | 2)
                    _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"}
                    ;;
                4 | 3 | 1) _comp_compgen_filedir ;;
            esac
            ;;
        --remove-follower | --remove-slave)
            case $args in
                3 | 1)
                    _comp_cmd_alternatives__installed ${dirs+"${dirs[@]}"}
                    ;;
                2) _comp_compgen_filedir ;;
            esac
            ;;
    esac
} &&
    complete -F _comp_cmd_alternatives alternatives
