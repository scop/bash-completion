# fio(1) completion                                        -*- shell-script -*-

_comp_cmd_fio__compgen_engines()
{
    _comp_compgen_split -F $'\t\n' -- "$("$1" --enghelp 2>/dev/null | command sed -ne '/^[[:space:]]/p')"
}

_comp_cmd_fio()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local REPLY
    case $prev in
        --help | --version)
            return
            ;;
        --debug)
            local opts=$("$1" --debug=help 2>/dev/null)
            opts=${opts##*:}
            _comp_delimited , -W "${opts//,/ }"
            return
            ;;
        --output-format)
            _comp_compgen -- -W "terse json json+ normal"
            return
            ;;
        --terse-version)
            _comp_compgen -- -W "2 3 4 5"
            return
            ;;
        --crctest)
            _comp_compgen_split -- "$("$1" --crctest=nonexistent 2>/dev/null)"
            return
            ;;
        --cmdhelp)
            _comp_compgen_split -- "$("$1" --cmdhelp=all 2>/dev/null | _comp_awk '{print $1}') all"
            return
            ;;
        --enghelp)
            _comp_cmd_fio__compgen_engines "$1"
            return
            ;;
        --eta)
            _comp_compgen -- -W "always never auto"
            return
            ;;
        --daemonize)
            _comp_compgen_filedir pid
            return
            ;;
        --client)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --remote-config)
            _comp_compgen_filedir '@(fio|job)'
            return
            ;;
        --idle-prof)
            _comp_compgen -- -W "system percpu calibrate"
            return
            ;;
        --inflate-log)
            _comp_compgen_filedir log
            return
            ;;
        --trigger-file)
            _comp_compgen_filedir
            return
            ;;
        --trigger | --trigger-remote)
            _comp_compgen_commands
            return
            ;;
        --aux-path)
            _comp_compgen_filedir -d
            return
            ;;
        --ioengine)
            _comp_cmd_fio__compgen_engines "$1"
            return
            ;;
        --exec_postrun | --exec_prerun)
            _comp_compgen_commands
            return
            ;;
        --uid)
            _comp_compgen_uids
            return
            ;;
        --gid)
            _comp_compgen_gids
            return
            ;;
        --?*)
            local -a cmdhelp
            _comp_split -l cmdhelp "$("$1" --cmdhelp="${prev#--}" 2>/dev/null)"
            case ${cmdhelp[*]-} in
                *"showing closest match"*)
                    # ignore
                    ;;
                *" type: boolean "* | *" type: empty or boolean "*)
                    _comp_compgen -- -W '0 1'
                    return
                    ;;
                *" valid values:"*)
                    # For example, for --kb_base=:
                    #        valid values: 1024       [...]
                    #                    : 1000       [...]
                    local line="" in_values=""
                    REPLY=()
                    for line in "${cmdhelp[@]}"; do
                        if [[ $in_values ]]; then
                            if [[ $line =~ ^[[:space:]]*:[[:space:]]*([^[:space:]]+) ]]; then
                                REPLY+=("${BASH_REMATCH[1]}")
                            else
                                break
                            fi
                        elif [[ $line =~ ^[[:space:]]*valid\ values:[[:space:]]*([^[:space:]]+) ]]; then
                            in_values=set
                            REPLY+=("${BASH_REMATCH[1]}")
                        fi
                    done
                    _comp_compgen -- -W '"${REPLY[@]}"'
                    return
                    ;;
            esac
            # else fallthrough
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -a split -- "$("$1" --cmdhelp=all 2>/dev/null |
            _comp_awk '{printf "--%s=\n", $1}')"
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir '@(fio|job)'
} &&
    complete -F _comp_cmd_fio fio

# ex: filetype=sh
