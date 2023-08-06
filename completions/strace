# bash completion for strace                               -*- shell-script -*-

_comp_cmd_strace()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    # check if we're still completing strace
    local offset=0 i
    for ((i = 1; i <= cword; i++)); do
        case ${words[i]} in
            -o | -e | -p)
                ((i++))
                continue
                ;;
            -*)
                continue
                ;;
        esac
        offset=$i
        break
    done

    if ((offset > 0)); then
        _comp_command_offset $offset
    else

        case $prev in
            -*e)
                if [[ $cur == *=* ]]; then
                    prev=${cur/=*/}
                    cur=${cur/*=/}

                    case $prev in
                        trace)
                            # Import arch-specific syscalls
                            #+ -- not foolproof IMHO --David Paleino
                            local define syscall rest
                            local -A syscalls
                            while read -r define syscall rest; do
                                [[ $define == "#define" &&
                                    $syscall =~ ^__NR_(.+) ]] &&
                                    syscalls[${BASH_REMATCH[1]}]=set
                            done 2>/dev/null </usr/include/asm/unistd.h
                            if ((${#syscalls[@]} == 0)); then
                                local unistd arch=$(command uname -m)
                                if [[ $arch == *86 ]]; then
                                    unistd=/usr/include/asm/unistd_32.h
                                else
                                    unistd=/usr/include/asm/unistd_64.h
                                fi
                                while read -r define syscall rest; do
                                    [[ $define == "#define" &&
                                        $syscall =~ ^__NR_(.+) ]] &&
                                        syscalls[${BASH_REMATCH[1]}]=set
                                done 2>/dev/null <$unistd
                            fi

                            _comp_compgen -- -W \
                                '${syscalls[@]+"${!syscalls[@]}"} file process
                                network signal ipc desc all none'
                            return
                            ;;
                    esac
                else
                    compopt -o nospace
                    _comp_compgen -- -S"=" -W 'trace abbrev verbose raw signal
                        read write'
                fi
                return
                ;;
            -*o)
                _comp_compgen_filedir
                return
                ;;
            -*p)
                _comp_compgen_pids
                return
                ;;
            -*S)
                _comp_compgen -- -W 'time calls name nothing'
                return
                ;;
            -*u)
                _comp_compgen_allowed_users
                return
                ;;
        esac

        if [[ $cur == -* ]]; then
            _comp_compgen_help -- -h
        else
            _comp_compgen_commands
        fi
    fi
} &&
    complete -F _comp_cmd_strace -o default strace

# ex: filetype=sh
