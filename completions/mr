# mr completion                                            -*- shell-script -*-

_comp_cmd_mr()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local help commands options

    help="$(PERLDOC_PAGER=cat PERLDOC=-otext "${1}" help 2>/dev/null)"

    commands="$(
        # shellcheck disable=SC2030
        printf %s "$help" | while read -r _ options cmd _; do
            [[ $options != "[options]" ]] || printf "%s\n" "$cmd"
        done
    )"
    # Split [online|offline] and remove `action` placeholder.
    commands="${commands//@(action|[\[\|\]])/ }"
    # Add standard aliases.
    commands="${commands} ci co ls"
    _comp_split commands "$commands"
    local IFS='|'
    local glob_commands="@(${commands[*]})"
    _comp_unlocal IFS

    # Determine if user has entered an `mr` command. Used to block top-level
    # (option and command) completions.
    local cmd has_cmd="" i
    for ((i = 1; i < cword; i++)); do
        # shellcheck disable=SC2053
        if [[ ${words[i]} == $glob_commands ]]; then
            cmd="${words[i]}"
            has_cmd=set
            break
        fi
    done

    # Complete options for specific commands.
    if [[ $has_cmd ]]; then
        case $cmd in
            bootstrap)
                _comp_compgen_filedir
                # Also complete stdin (-) as a potential bootstrap source.
                if [[ ! ${cur} || $cur == - ]] && [[ $prev != - ]]; then
                    COMPREPLY+=(-)
                fi
                return
                ;;
            clean)
                if [[ ${cur} == -* ]]; then
                    _comp_compgen -- -W '-f'
                fi
                return
                ;;
            commit | ci | record)
                if [[ ${cur} == -* ]]; then
                    _comp_compgen -- -W '-m'
                fi
                return
                ;;
            run)
                _comp_compgen_commands
                return
                ;;
            *)
                # Do not complete any other command.
                return
                ;;
        esac
    fi

    # Complete top-level options and commands.
    local noargopts='!(-*|*[cd]*)'
    # shellcheck disable=SC2254
    case $prev in
        --config | -${noargopts}c)
            _comp_compgen_filedir
            return
            ;;
        --directory | -${noargopts}d)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -Rv options help - <<<"$help"
        # -X '-[a-z]': Remove short options (all have compatible long options).
        # -X '--path': Remove deprecated options.
        _comp_compgen -- -W '"${options[@]}"' -X '@(-[a-z]|--path)'
    else
        _comp_compgen -- -W '"${commands[@]}"'
    fi
} &&
    complete -F _comp_cmd_mr mr

# ex: filetype=sh
