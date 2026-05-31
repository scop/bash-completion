# Deprecated bash_completion functions and variables       -*- shell-script -*-

_comp_deprecate_func 2.12 _userland _comp_userland
_comp_deprecate_func 2.12 _sysvdirs _comp_sysvdirs
_comp_deprecate_func 2.12 _have _comp_have_command
_comp_deprecate_func 2.12 _rl_enabled _comp_readline_variable_on
_comp_deprecate_func 2.12 _command_offset _comp_command_offset
_comp_deprecate_func 2.12 _command _comp_command
_comp_deprecate_func 2.12 _root_command _comp_root_command
_comp_deprecate_func 2.12 _xfunc _comp_xfunc
_comp_deprecate_func 2.12 _upvars _comp_upvars
_comp_deprecate_func 2.12 _get_comp_words_by_ref _comp_get_words
_comp_deprecate_func 2.12 _known_hosts_real _comp_compgen_known_hosts
_comp_deprecate_func 2.12 __ltrim_colon_completions _comp_ltrim_colon_completions
_comp_deprecate_func 2.12 _variables _comp_compgen_variables
_comp_deprecate_func 2.12 _signals _comp_compgen_signals
_comp_deprecate_func 2.12 _mac_addresses _comp_compgen_mac_addresses
_comp_deprecate_func 2.12 _available_interfaces _comp_compgen_available_interfaces
_comp_deprecate_func 2.12 _configured_interfaces _comp_compgen_configured_interfaces
_comp_deprecate_func 2.12 _ip_addresses _comp_compgen_ip_addresses
_comp_deprecate_func 2.12 _kernel_versions _comp_compgen_kernel_versions
_comp_deprecate_func 2.12 _uids _comp_compgen_uids
_comp_deprecate_func 2.12 _gids _comp_compgen_gids
_comp_deprecate_func 2.12 _xinetd_services _comp_compgen_xinetd_services
_comp_deprecate_func 2.12 _services _comp_compgen_services
_comp_deprecate_func 2.12 _bashcomp_try_faketty _comp_try_faketty
_comp_deprecate_func 2.12 _expand _comp_expand
_comp_deprecate_func 2.12 _pids _comp_compgen_pids
_comp_deprecate_func 2.12 _pgids _comp_compgen_pgids
_comp_deprecate_func 2.12 _pnames _comp_compgen_pnames
_comp_deprecate_func 2.12 _modules _comp_compgen_kernel_modules
_comp_deprecate_func 2.12 _installed_modules _comp_compgen_inserted_kernel_modules
_comp_deprecate_func 2.12 _usergroup _comp_compgen_usergroups
_comp_deprecate_func 2.12 _complete_as_root _comp_as_root
_comp_deprecate_func 2.12 __load_completion _comp_load

# completers
_comp_deprecate_func 2.12 _service _comp_complete_service
_comp_deprecate_func 2.12 _user_at_host _comp_complete_user_at_host
_comp_deprecate_func 2.12 _known_hosts _comp_complete_known_hosts
_comp_deprecate_func 2.12 _longopt _comp_complete_longopt
_comp_deprecate_func 2.12 _filedir_xspec _comp_complete_filedir_xspec
_comp_deprecate_func 2.12 _minimal _comp_complete_minimal

_comp_deprecate_var 2.12 COMP_FILEDIR_FALLBACK BASH_COMPLETION_FILEDIR_FALLBACK
_comp_deprecate_var 2.12 COMP_KNOWN_HOSTS_WITH_AVAHI BASH_COMPLETION_KNOWN_HOSTS_WITH_AVAHI
_comp_deprecate_var 2.12 COMP_KNOWN_HOSTS_WITH_HOSTFILE BASH_COMPLETION_KNOWN_HOSTS_WITH_HOSTFILE

# @deprecated 2.12 Use `_comp_xspecs`
declare -Ag _xspecs

# Backwards compatibility for compat completions that use have().
# @deprecated 1.90 should no longer be used; generally not needed with
#   dynamically loaded completions, and _comp_have_command is suitable for
#   runtime use.
# shellcheck disable=SC2317 # available at load time only
have()
{
    unset -v have
    _comp_have_command "$1" && have=yes
}

# This function shell-quotes the argument
# @deprecated 2.12 Use `_comp_quote` instead.  Note that `_comp_quote` stores
#   the results in the variable `REPLY` instead of writing them to stdout.
quote()
{
    local quoted=${1//\'/\'\\\'\'}
    printf "'%s'" "$quoted"
}

# @deprecated 2.12 Use `_comp_quote_compgen`
quote_readline()
{
    local REPLY
    _comp_quote_compgen "$1"
    printf %s "$REPLY"
}

# This function is the same as `_comp_quote_compgen`, but receives the second
# argument specifying the variable name to store the result.
# @param $1  Argument to quote
# @param $2  Name of variable to return result to
# @deprecated 2.12 Use `_comp_quote_compgen "$1"` instead.  Note that
# `_comp_quote_compgen` stores the result in a fixed variable `REPLY`.
_quote_readline_by_ref()
{
    [[ $2 == REPLY ]] || local REPLY
    _comp_quote_compgen "$1"
    [[ $2 == REPLY ]] || printf -v "$2" %s "$REPLY"
}

# This function shell-dequotes the argument
# @deprecated 2.12 Use `_comp_dequote' instead.  Note that `_comp_dequote`
#   stores the results in the array `REPLY` instead of writing them to stdout.
dequote()
{
    local REPLY
    _comp_dequote "$1"
    local rc=$?
    printf %s "$REPLY"
    return $rc
}

# Assign variable one scope above the caller
# Usage: local "$1" && _upvar $1 "value(s)"
# @param $1  Variable name to assign value to
# @param $*  Value(s) to assign.  If multiple values, an array is
#            assigned, otherwise a single value is assigned.
# NOTE: For assigning multiple variables, use '_comp_upvars'.  Do NOT
#       use multiple '_upvar' calls, since one '_upvar' call might
#       reassign a variable to be used by another '_upvar' call.
# @see https://fvue.nl/wiki/Bash:_Passing_variables_by_reference
# @deprecated 2.10 Use `_comp_upvars' instead
_upvar()
{
    echo "bash_completion: $FUNCNAME: deprecated function," \
        "use _comp_upvars instead" >&2
    if unset -v "$1"; then # Unset & validate varname
        # shellcheck disable=SC2140  # TODO
        if (($# == 2)); then
            eval "$1"=\"\$2\" # Return single value
        else
            eval "$1"=\(\"\$"{@:2}"\"\) # Return array
        fi
    fi
}

# Get the word to complete.
# This is nicer than ${COMP_WORDS[COMP_CWORD]}, since it handles cases
# where the user is completing in the middle of a word.
# (For example, if the line is "ls foobar",
# and the cursor is here -------->   ^
# @param $1 string  Characters out of $COMP_WORDBREAKS which should NOT be
#     considered word breaks. This is useful for things like scp where
#     we want to return host:path and not only path, so we would pass the
#     colon (:) as $1 in this case.
# @param $2 integer  Index number of word to return, negatively offset to the
#     current word (default is 0, previous is 1), respecting the exclusions
#     given at $1.  For example, `_get_cword "=:" 1' returns the word left of
#     the current word, respecting the exclusions "=:".
# @deprecated 1.2 Use `_comp_get_words cur' instead
# @see _comp_get_words()
_get_cword()
{
    local LC_CTYPE=C
    local cword words
    _comp__reassemble_words "${1-}" words cword

    # return previous word offset by $2
    if [[ ${2-} && ${2//[^0-9]/} ]]; then
        printf "%s" "${words[cword - $2]}"
    elif ((${#words[cword]} == 0 && COMP_POINT == ${#COMP_LINE})); then
        : # nothing
    else
        local i
        local cur=$COMP_LINE
        local index=$COMP_POINT
        for ((i = 0; i <= cword; ++i)); do
            # Current word fits in $cur, and $cur doesn't match cword?
            while [[ ${#cur} -ge ${#words[i]} &&
                ${cur:0:${#words[i]}} != "${words[i]}" ]]; do
                # Strip first character
                cur=${cur:1}
                # Decrease cursor position, staying >= 0
                ((index > 0)) && ((index--))
            done

            # Does found word match cword?
            if ((i < cword)); then
                # No, cword lies further;
                local old_size=${#cur}
                cur=${cur#"${words[i]}"}
                local new_size=${#cur}
                ((index -= old_size - new_size))
            fi
        done

        if [[ ${words[cword]:0:${#cur}} != "$cur" ]]; then
            # We messed up! At least return the whole word so things
            # keep working
            printf "%s" "${words[cword]}"
        else
            printf "%s" "${cur:0:index}"
        fi
    fi
}

# Get word previous to the current word.
# This is a good alternative to `prev=${COMP_WORDS[COMP_CWORD-1]}' because bash4
# will properly return the previous word with respect to any given exclusions to
# COMP_WORDBREAKS.
# @deprecated 1.2 Use `_comp_get_words cur prev' instead
# @see _comp_get_words()
#
_get_pword()
{
    if ((COMP_CWORD >= 1)); then
        _get_cword "${@-}" 1
    fi
}

# Get real command.
# @deprecated 2.12 Use `_comp_realcommand` instead.
# Note that `_comp_realcommand` stores the result in the variable `REPLY`
# instead of writing it to stdout.
_realcommand()
{
    local REPLY
    _comp_realcommand "$1"
    local rc=$?
    printf "%s\n" "$REPLY"
    return $rc
}

# Initialize completion and deal with various general things: do file
# and variable completion where appropriate, and adjust prev, words,
# and cword as if no redirections exist so that completions do not
# need to deal with them.  Before calling this function, make sure
# cur, prev, words, and cword are local, ditto split if you use -s.
#
# Options:
#     -n EXCLUDE  Passed to _comp_get_words -n with redirection chars
#     -e XSPEC    Passed to _filedir as first arg for stderr redirections
#     -o XSPEC    Passed to _filedir as first arg for other output redirections
#     -i XSPEC    Passed to _filedir as first arg for stdin redirections
#     -s          Split long options with _comp__split_longopt, implies -n =
# @var[out] cur       Reconstructed current word
# @var[out] prev      Reconstructed previous word
# @var[out] words     Reconstructed words
# @var[out] cword     Current word index in `words`
# @var[out,opt] split When "-s" is specified, `"true"/"false"` is set depending
#                     on whether the split happened.
# @return  True (0) if completion needs further processing,
#          False (> 0) no further processing is necessary.
#
# @deprecated 2.12 Use the new interface `_comp_initialize`.  The new interface
# supports the same set of options.  The new interface receives additional
# arguments $1 (command name), $2 (part of current word before the cursor), and
# $3 (previous word) that are specified to the completion function by Bash.
# When `-s` is specified, instead of variable `split`, the new interface sets
# variable `was_split` to the value "set"/"" when the split happened/not
# happened.
_init_completion()
{
    local was_split
    _comp_initialize "$@"
    local rc=$?

    # When -s is specified, convert "split={set,}" to "split={true,false}"
    local flag OPTIND=1 OPTARG="" OPTERR=0
    while getopts "n:e:o:i:s" flag "$@"; do
        case $flag in
            [neoi]) ;;
            s)
                if [[ $was_split ]]; then
                    split=true
                else
                    split=false
                fi
                break
                ;;
        esac
    done

    return "$rc"
}

# @deprecated 2.12 Use the variable `_comp_backup_glob` instead.  This is the
# backward-compatibility name.
# shellcheck disable=SC2154  # defined in the main "bash_completion"
_backup_glob=$_comp_backup_glob

# @deprecated 2.12 use `_comp_cmd_cd` instead.
_cd()
{
    declare -F _comp_cmd_cd &>/dev/null || __load_completion cd
    _comp_cmd_cd "$@"
}

# @deprecated 2.12 Use `_comp_command_offset` instead.  Note that the new
# interface `_comp_command_offset` is changed to receive an index in
# `words` instead of that in `COMP_WORDS` as `_command_offset` did.
_command_offset()
{
    # We unset the shell variable `words` locally to tell
    # `_comp_command_offset` that the index is intended to be that in
    # `COMP_WORDS` instead of `words`.
    local words
    unset -v words
    _comp_command_offset "$@"
}

# @deprecated 2.12 Use `_comp_compgen -a filedir`
_filedir()
{
    _comp_compgen -a filedir "$@"
}

# Perform tilde (~) completion
# @return  True (0) if completion needs further processing,
#          False (1) if tilde is followed by a valid username, completions are
#          put in COMPREPLY and no further processing is necessary.
# @deprecated 2.12 Use `_comp_compgen -c CUR tilde [-d]`.  Note that the exit
# status of `_comp_compgen_tilde` is flipped.  It returns 0 when the tilde
# completions are attempted, or otherwise 1.
_tilde()
{
    ! _comp_compgen -c "$1" tilde
}

# Helper function for _parse_help and _parse_usage.
# @return True (0) if an option was found, False (> 0) otherwise
# @deprecated 2.12 Use _comp_compgen_help__parse
__parse_options()
{
    local -a _options=()
    _comp_compgen_help__parse "$1"
    printf '%s\n' "${_options[@]}"
}

# Parse GNU style help output of the given command.
# @param $1  command; if "-", read from stdin and ignore rest of args
# @param $2  command options (default: --help)
# @deprecated 2.12 Use `_comp_compgen_help`.  `COMPREPLY=($(compgen -W
#   '$(_parse_help "$1" ...)' -- "$cur"))` can be replaced with
#   `_comp_compgen_help [-- ...]`.  Also, `var=($(_parse_help "$1" ...))` can
#   be replaced with `_comp_compgen -Rv var help [-- ...]`.
_parse_help()
{
    local -a args
    if [[ $1 == - ]]; then
        args=(-)
    else
        local REPLY opt IFS=$' \t\n'
        _comp_dequote "$1"
        _comp_split opt "${2:---help}"
        args=(-c "$REPLY" ${opt[@]+"${opt[@]}"})
    fi
    local -a REPLY=()
    _comp_compgen -Rv REPLY help "${args[@]}" || return 1
    ((${#REPLY[@]})) && printf '%s\n' "${REPLY[@]}"
    return 0
}

# Parse BSD style usage output (options in brackets) of the given command.
# @param $1  command; if "-", read from stdin and ignore rest of args
# @param $2  command options (default: --usage)
# @deprecated 2.12 Use `_comp_compgen_usage`.  `COMPREPLY=($(compgen -W
#   '$(_parse_usage "$1" ...)' -- "$cur"))` can be replaced with
#   `_comp_compgen_usage [-- ...]`. `var=($(_parse_usage "$1" ...))` can be
#   replaced with `_comp_compgen -Rv var usage [-- ...]`.
_parse_usage()
{
    local -a args
    if [[ $1 == - ]]; then
        args=(-)
    else
        local REPLY opt IFS=$' \t\n'
        _comp_dequote "$1"
        _comp_split opt "${2:---usage}"
        args=(-c "$REPLY" ${opt[@]+"${opt[@]}"})
    fi
    local -a REPLY=()
    _comp_compgen -Rv REPLY usage "${args[@]}" || return 1
    ((${#REPLY[@]})) && printf '%s\n' "${REPLY[@]}"
    return 0
}

# @deprecated 2.12 Use `_comp_get_ncpus`.
_ncpus()
{
    local REPLY
    _comp_get_ncpus
    printf %s "$REPLY"
}

# Expand variable starting with tilde (~).
# We want to expand ~foo/... to /home/foo/... to avoid problems when
# word-to-complete starting with a tilde is fed to commands and ending up
# quoted instead of expanded.
# Only the first portion of the variable from the tilde up to the first slash
# (~../) is expanded.  The remainder of the variable, containing for example
# a dollar sign variable ($) or asterisk (*) is not expanded.
#
# @deprecated 2.12 Use `_comp_expand_tilde`.  The new function receives the
# value instead of a variable name as $1 and always returns the result to the
# variable `REPLY`.
__expand_tilde_by_ref()
{
    [[ ${1+set} ]] || return 0
    [[ $1 == REPLY ]] || local REPLY
    _comp_expand_tilde "${!1-}"
    # shellcheck disable=SC2059
    [[ $1 == REPLY ]] || printf -v "$1" "$REPLY"
}

# @deprecated 2.12 Use `_comp_compgen -a cd_devices`
_cd_devices()
{
    _comp_compgen -a cd_devices
}

# @deprecated 2.12 Use `_comp_compgen -a dvd_devices`
_dvd_devices()
{
    _comp_compgen -a dvd_devices
}

# @deprecated 2.12 Use `_comp_compgen -a pci_ids`
_pci_ids()
{
    _comp_compgen -a pci_ids
}

# @deprecated 2.12 Use `_comp_compgen -a usb_ids`
_usb_ids()
{
    _comp_compgen -a usb_ids
}

# @deprecated 2.12 Use `_comp_compgen -a terms`
_terms()
{
    _comp_compgen -a terms
}

# @deprecated 2.12 Use `_comp_compgen -c "${prefix:-$cur}" allowed_users`
_allowed_users()
{
    _comp_compgen -c "${1:-$cur}" allowed_users
}

# @deprecated 2.12 Use `_comp_compgen -c "${prefix:-$cur}" allowed_groups`
_allowed_groups()
{
    _comp_compgen -c "${1:-$cur}" allowed_groups
}

# @deprecated 2.12 Use `_comp_compgen -a shells`
_shells()
{
    _comp_compgen -a shells
}

# @deprecated 2.12 Use `_comp_compgen -a fstypes`
_fstypes()
{
    _comp_compgen -a fstypes
}

# This function returns the first argument, excluding options
# @deprecated 2.12 Use `_comp_get_first_arg`.  Note that the new function
# `_comp_get_first_arg` operates on `words` and `cword` instead of `COMP_WORDS`
# and `COMP_CWORD`.  The new function considers a command-line argument after
# `--` as an argument.  The new function returns the result in variable `REPLY`
# instead of `arg`.
_get_first_arg()
{
    local i

    arg=
    for ((i = 1; i < COMP_CWORD; i++)); do
        if [[ ${COMP_WORDS[i]} != -* ]]; then
            arg=${COMP_WORDS[i]}
            break
        fi
    done
}

# This function counts the number of args, excluding options
# @param $1 chars  Characters out of $COMP_WORDBREAKS which should
#     NOT be considered word breaks. See _comp__reassemble_words.
# @param $2 glob   Options whose following argument should not be counted
# @param $3 glob   Options that should be counted as args
# @var[out] args   Return the number of arguments
# @deprecated 2.12 Use `_comp_count_args`.  Note that the new function
# `_comp_count_args` returns the result in variable `REPLY` instead of `args`.
# In the new function, `-` is also counted as an argument.  The new function
# counts all the arguments after `--`.
# shellcheck disable=SC2178 # assignments are not intended for global "args"
_count_args()
{
    local i cword words
    _comp__reassemble_words "${1-}" words cword

    args=1
    for ((i = 1; i < cword; i++)); do
        # shellcheck disable=SC2053
        if [[ ${words[i]} != -* && ${words[i - 1]} != ${2-} ||
            ${words[i]} == ${3-} ]]; then
            ((args++))
        fi
    done
}

# @deprecated 2.12 Use `_comp_load -D -- CommandName` to load the completion,
# or use `_comp_complete_load` as a completion function specified to `complete
# -F`.
_completion_loader()
{
    # We call `_comp_complete_load` instead of `_comp_load -D` in case that
    # `_completion_loader` is used without an argument or `_completion_loader`
    # is specified to `complete -F` by a user.
    _comp_complete_load "$@"
}
# ex: filetype=sh
