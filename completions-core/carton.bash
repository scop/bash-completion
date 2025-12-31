# carton(3pm) completion                                   -*- shell-script -*-

_comp_cmd_carton__commands()
{
    local cmds=$("$1" usage 2>&1 |
        command sed -ne '/.*command.* is one of/{n;p;q;}')
    _comp_compgen -aF $' \t\n,' -- -W "$cmds"
}

_comp_cmd_carton__command_help()
{
    local help=$(PERLDOC_PAGER=cat PERLDOC=-otext "$1" -h "$2" 2>&1)
    _comp_compgen -a -- -W '$help'
}

_comp_cmd_carton()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local i command="" has_command=""
    for ((i = 1; i < cword; i++)); do
        case ${words[i]} in
            -*) ;;
            *)
                command=${words[i]}
                has_command=set
                break
                ;;
        esac
    done

    if [[ ! $has_command ]]; then
        _comp_cmd_carton__commands "$1"
        return
    fi

    case $prev in
        --version | --help | -[vh])
            return
            ;;
        --cpanfile)
            if [[ $command == install ]]; then
                _comp_compgen_filedir
                return
            fi
            ;;
        --path)
            if [[ $command == install ]]; then
                _comp_compgen_filedir -d
                return
            fi
            ;;
        --without)
            if [[ $command == install ]]; then
                local phases="configure build test runtime develop"
                _comp_compgen -a -- -W '$phases'
                return
            fi
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        [[ $command == @(help|usage) ]] || COMPREPLY=(--help)
        _comp_cmd_carton__command_help "$1" "$command"
    fi

    case $command in
        exec)
            # skip all the options --, -v, etc. and identify the command name
            # position.
            for ((i++; i < cword; i++)); do
                case ${words[i]} in
                    --)
                        ((i++))
                        break
                        ;;
                    -*) ;;
                    *) break ;;
                esac
            done

            _comp_command_offset "$i"
            return
            ;;
        show | update)
            : # TODO modules completion
            ;;
    esac
} &&
    complete -F _comp_cmd_carton carton

# ex: filetype=sh
