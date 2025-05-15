# tmux(1) completion                                       -*- shell-script -*-
# SPDX-License-Identifier: GPL-2.0-or-later OR ISC

# Log a message to help with debugging.
# If BASH_COMPLETION_DEBUG is set, it will be printed to stderr.
# When running with `set -x`, the _comp_cmd_tmux__log call itself will be
# printed.
#
# @param $1 Message to log
_comp_cmd_tmux__log()
{
    if [[ ${BASH_COMPLETION_DEBUG-} ]]; then
        printf 'tmux bash completion: %s\n' "$1" >&2
    fi
}

# Run the tmux command being completed.
#
# @param $@ args to tmux
_comp_cmd_tmux__run()
{
    local -a REPLY
    _comp_dequote "${comp_args[0]-}" || REPLY=("${comp_args[0]-}")
    LC_ALL=C "${REPLY[0]}" "$@"
}

# Parse usage output from tmux.
#
# @param $1 Usage from tmux, not including the (sub)command name.
# @var[out] options associative array mapping options to their value types, or
#     to the empty string if the option doesn't take a value
# @var[out] args indexed array of positional arg types
_comp_cmd_tmux__parse_usage()
{
    options=()
    args=()

    local i j
    local words
    _comp_split words "$1"
    for ((i = 0; i < ${#words[@]}; i++)); do
        case ${words[i]} in
            "[-"*"]")
                # One or more options that don't take arguments, either of the
                # form `[-abc]` or `[-a|-b|-c]`
                for ((j = 2; j < ${#words[i]} - 1; j++)); do
                    if [[ ${words[i]:j:1} != [-\|] ]]; then
                        options+=(["-${words[i]:j:1}"]="")
                    fi
                done
                ;;
            "[-"*)
                # One option that does take an argument.
                if [[ ${words[i + 1]-} != *"]" ]]; then
                    _comp_cmd_tmux__log \
                        "Can't parse option: '${words[*]:i:2}' in '$1'"
                    break
                fi
                options+=(["${words[i]#"["}"]="${words[i + 1]%"]"}")
                ((i++))
                ;;
            -*)
                _comp_cmd_tmux__log "Can't parse option '${words[i]}' in '$1'"
                break
                ;;
            *)
                # Start of positional arguments.
                args=("${words[@]:i}")
                break
                ;;
        esac
    done

    if [[ ${BASH_COMPLETION_DEBUG-} || -o xtrace ]]; then
        local arg
        for arg in "${!options[@]}"; do
            _comp_cmd_tmux__log "option: ${arg} ${options["$arg"]}"
        done
        for arg in "${args[@]}"; do
            _comp_cmd_tmux__log "arg: ${arg}"
        done
    fi
}

# Complete a value either as the argument to an option or as a positional arg.
#
# @param $1 subcommand that the value is for, or 'tmux' if it's top-level
# @param $2 type of the value, from _comp_cmd_tmux__parse_usage()
_comp_cmd_tmux__value()
{
    local subcommand=$1 option_type=$2
    _comp_cmd_tmux__log \
        "Trying to complete '$option_type' for subcommand '$subcommand'"

    # To get a list of these argument types, look at `tmux -h` and:
    #
    # tmux list-commands -F "#{command_list_usage}" |
    #   sed 's/[][ ]/\n/g' |
    #   grep -v ^- |
    #   sort -u
    #
    # TODO: Complete more option types.
    case $option_type in
        command)
            _comp_compgen_split -l -- "$(_comp_cmd_tmux__run \
                list-commands -F "#{command_list_name}")"
            ;;
        directory | *-directory)
            _comp_compgen_filedir -d
            ;;
        file | *-file | path | *-path)
            _comp_compgen_filedir
            ;;
    esac
}

# Parse command line options to tmux or a subcommand.
#
# @param $@ args to tmux or a subcommand, starting with the (sub)command
#     itself, ending before the current word to complete
# @var[in] options from _comp_cmd_tmux__parse_usage()
# @var[out] option_type if the word to complete is the value of an option, this
#     is the type of that value, otherwise it's empty
# @var[out] positional_start if option_type is empty, index in $@ of the first
#     positional argument, or the last index plus 1 if the next word is the
#     first positional argument, or -1 if the next word could be either the
#     first positional argument or another option
_comp_cmd_tmux__options()
{
    local command_args=("$@")
    option_type=""
    positional_start=-1

    local i
    for ((i = 1; i < ${#command_args[@]}; i++)); do
        if [[ $option_type ]]; then
            # arg to the previous option
            option_type=""
        elif [[ ${command_args[i]} == -- ]]; then
            option_type=""
            ((positional_start = i + 1))
            return
        elif [[ ${command_args[i]} == -?* ]]; then
            # 1 or more options, possibly also with the value of an option.
            # E.g., if `-a` and `-b` take no values and `-c` does, `-ab` would
            # be equivalent to `-a -b` and `-acb` would be `-a` and `-c` with a
            # value of `b`.
            local j
            for ((j = 1; j < ${#command_args[i]}; j++)); do
                if [[ $option_type ]]; then
                    # arg has both the option and its value
                    option_type=""
                    break
                fi
                option_type=${options["-${command_args[i]:j:1}"]-}
            done
        else
            # first positional arg
            ((positional_start = i))
            return
        fi
    done
}

# Complete arguments to a nested command.
#
# @param $1 the arg type of the command, e.g., command or shell-command
# @param $2... args to the command, starting with the command itself, ending
#     before the current word to complete
_comp_cmd_tmux__nested_arguments()
{
    local arg_type="$1"
    shift
    _comp_cmd_tmux__log \
        "Attempting completion for arguments to '$1' of type '$arg_type'"

    case $arg_type in
        command)
            _comp_cmd_tmux__subcommand "$@"
            ;;
    esac
}

# Complete arguments to a subcommand.
#
# @param $@ the subcommand followed by its args, ending before the current word
#     to complete
_comp_cmd_tmux__subcommand()
{
    local subcommand_args=("$@")
    local usage=$(_comp_cmd_tmux__run list-commands \
        -F "#{command_list_name} #{command_list_usage}" -- "$1" 2>/dev/null)
    if [[ ! $usage ]]; then
        _comp_cmd_tmux__log "Unknown tmux subcommand: '$1'"
        return
    fi
    local subcommand=${usage%% *} # not $1, because it could be an alias
    _comp_cmd_tmux__log "Attempting completion for 'tmux $subcommand'"

    local -A options
    local -a args
    _comp_cmd_tmux__parse_usage "${usage#* }"

    local option_type
    local positional_start
    _comp_cmd_tmux__options "${subcommand_args[@]}"

    if [[ $option_type ]]; then
        _comp_cmd_tmux__value "$subcommand" "$option_type"
        return
    elif ((positional_start < 0)) && [[ $cur == -* ]]; then
        _comp_compgen -- -W '"${!options[@]}"'
        return
    elif ((positional_start < 0)); then
        # $cur (one past the end of subcommand_args) is the first positional
        # arg
        positional_start=${#subcommand_args[@]}
    fi

    if [[ $subcommand == display-menu ]]; then
        # display-menu has a non-trivial repeating pattern of positional args
        # that would need custom logic to support correctly, and it's probably
        # used in config files or shell scripts more than interactively anyway.
        _comp_cmd_tmux__log \
            "Not completing positional args for 'tmux $subcommand'"
        return
    fi

    _comp_cmd_tmux__log \
        "'tmux $subcommand' first positional arg: '${subcommand_args[positional_start]-}'"

    local args_index=$positional_start
    local usage_args_index
    local prev_arg_type=""
    for ((\
    usage_args_index = 0;  \
    usage_args_index < ${#args[@]};  \
    args_index++, usage_args_index++)); do
        local arg_type=${args[usage_args_index]##+(\[)}
        arg_type=${arg_type%%+(\])}
        if [[ $arg_type == ... ]]; then
            if ((usage_args_index == 0)); then
                _comp_cmd_tmux__log "'tmux $subcommand' first arg is '...'"
                return
            elif ((usage_args_index != ${#args[@]} - 1)); then
                _comp_cmd_tmux__log \
                    "'tmux $subcommand' usage has '...' before last arg"
                return
            fi
            # https://man.openbsd.org/style says "Usage statements should take
            # the same form as the synopsis in manual pages."
            # https://mandoc.bsd.lv/mdoc/intro/synopsis_util.html says "Some
            # commands can optionally take more than one argument of the same
            # kind. This is indicated by an ellipsis trailing the respective Ar
            # macro." tmux seems to mostly use `...` in that way to only repeat
            # the previous argument. In display-menu it uses `...` to repeat
            # all arguments instead, but that subcommand is explicitly ignored
            # above.
            _comp_cmd_tmux__value "$subcommand" "$prev_arg_type"
            return
        elif [[ $arg_type == argument ]]; then
            # New-style usage after
            # https://github.com/tmux/tmux/commit/68ffe654990764ed5bdb7efb88e4d01b921fd3d5
            # (2025-04-09) ends in `argument ...`
            if ((usage_args_index == ${#args[@]} - 2)) &&
                [[ ${args[-1]-} == *("[")...*("]") ]]; then
                _comp_cmd_tmux__nested_arguments \
                    "$prev_arg_type" \
                    "${subcommand_args[@]:args_index-1}"
                return
            else
                _comp_cmd_tmux__log \
                    "'tmux $subcommand' has unsupported 'argument' in usage"
                return
            fi
        elif [[ $arg_type == arguments ]]; then
            # Old-style usage before
            # https://github.com/tmux/tmux/commit/68ffe654990764ed5bdb7efb88e4d01b921fd3d5
            # (2025-04-09) ends in `arguments`
            if ((usage_args_index == ${#args[@]} - 1)); then
                _comp_cmd_tmux__nested_arguments \
                    "$prev_arg_type" \
                    "${subcommand_args[@]:args_index-1}"
                return
            else
                _comp_cmd_tmux__log \
                    "'tmux $subcommand' has unsupported 'arguments' in usage"
                return
            fi
        elif ((args_index == ${#subcommand_args[@]})); then
            # The usage arg is 1 past the end of $subcommand_args, so complete
            # it.
            _comp_cmd_tmux__value "$subcommand" "$arg_type"
            return
        fi
        prev_arg_type=$arg_type
    done

    _comp_cmd_tmux__log "Too many args to 'tmux $subcommand'"
}

_comp_cmd_tmux()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local usage
    usage=$(_comp_cmd_tmux__run -h 2>&1)
    # Before https://github.com/tmux/tmux/pull/4455 (merged 2025-04-09), `-h`
    # produced usage information because it was an error, so we have to trim
    # the error message too.
    usage=${usage#$'tmux: unknown option -- h\n'}
    usage=${usage#usage: tmux }

    local -A options
    local -a args
    _comp_cmd_tmux__parse_usage "$usage"

    local option_type
    local positional_start
    _comp_cmd_tmux__options "${words[@]:0:cword}"

    if [[ $option_type ]]; then
        _comp_cmd_tmux__value tmux "$option_type"
        return
    elif ((positional_start < 0)) && [[ $cur == -* ]]; then
        _comp_compgen -- -W '"${!options[@]}"'
        return
    elif ((positional_start < 0)); then
        ((positional_start = cword))
    fi

    local i
    local -a REPLY
    local subcommand_start=$positional_start
    for ((i = positional_start; i < cword; i++)); do
        if _comp_dequote "${words[i]}" && [[ ${REPLY[-1]-} =~ (\\*)\;$ ]] &&
            ((${#BASH_REMATCH[1]} % 2 == 0)); then
            # end of current command
            ((subcommand_start = i + 1))
        fi
    done

    if ((cword == subcommand_start)); then
        _comp_cmd_tmux__value tmux command
    else
        _comp_cmd_tmux__subcommand \
            "${words[@]:subcommand_start:cword-subcommand_start}"
    fi
} &&
    complete -F _comp_cmd_tmux tmux

# ex: filetype=sh
