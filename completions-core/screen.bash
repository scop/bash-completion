# bash completion for screen                               -*- shell-script -*-

_comp_cmd_screen__sessions()
{
    local -a sessions
    _comp_split sessions "$(command screen -ls | command sed -ne \
        's|^\t\{1,\}\([0-9]\{1,\}\.[^\t]\{1,\}\).*'"$1"'.*$|\1|p')" || return
    if [[ $cur == +([0-9])?(.*) ]]; then
        # Complete sessions including pid prefixes
        _comp_compgen -- -W '"${sessions[@]}"'
    else
        # Create unique completions, dropping pids where possible
        local -A res
        local i tmp
        for i in "${sessions[@]}"; do
            res[${i/#+([0-9])./}]+=" $i"
        done
        for i in "${!res[@]}"; do
            [[ ${res[i]} == \ *\ * ]] && tmp+=" ${res[i]}" || tmp+=" $i"
        done
        _comp_compgen -- -W '$tmp'
    fi
} &&
    _comp_cmd_screen()
    {
        local cur prev words cword comp_args
        _comp_initialize -- "$@" || return

        if ((cword == 1)); then
            if [[ $cur == /dev* ]]; then
                _comp_expand_glob COMPREPLY '/dev/serial/*/* /dev/ttyUSB* /dev/ttyACM*' &&
                    _comp_compgen -- -W '"${COMPREPLY[@]}"'
                return
            fi
            if [[ $cur == //* ]]; then
                _comp_compgen -- -W '//telnet'
                return
            fi
        fi

        case ${words[1]} in
            /dev*)
                if ((cword == 2)); then
                    _comp_compgen -- -W '110 300 600 1200 2400 4800 9600 14400
                        19200 38400 57600 115200 128000 256000'
                    # TODO more, comma separated options
                fi
                return
                ;;
            //telnet)
                ((cword == 2)) && _comp_compgen_known_hosts -- "$cur"
                return
                ;;
        esac

        if ((cword > 2)); then
            case ${words[cword - 2]} in
                -*[dD])
                    _comp_cmd_screen__sessions
                    return
                    ;;
            esac
        fi

        local i
        for ((i = 1; i <= cword; i++)); do
            case ${words[i]} in
                -*[rRdDxscTehpSt])
                    ((i++))
                    continue
                    ;;
                -*)
                    continue
                    ;;
            esac

            _comp_command_offset $i
            return
        done

        case $prev in
            -*[rR])
                # list detached
                _comp_cmd_screen__sessions 'Detached'
                return
                ;;
            -*[dD])
                # list attached
                _comp_cmd_screen__sessions 'Attached'
                return
                ;;
            -*x)
                # list both
                _comp_cmd_screen__sessions
                return
                ;;
            -*s)
                _comp_compgen_shells
                return
                ;;
            -*c)
                _comp_compgen_filedir
                return
                ;;
            -T)
                _comp_compgen_terms
                return
                ;;
            -*[ehpSt])
                return
                ;;
        esac

        if [[ $cur == -* ]]; then
            _comp_compgen_help
        fi
    } &&
        complete -F _comp_cmd_screen screen

# ex: filetype=sh
