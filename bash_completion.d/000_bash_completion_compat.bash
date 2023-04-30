# Deprecated bash_completion functions and variables        -*- shell-script -*-

_comp_deprecate_func _userland _comp_userland
_comp_deprecate_func _sysvdirs _comp_sysvdirs
_comp_deprecate_func _have _comp_have_command
_comp_deprecate_func _rl_enabled _comp_readline_variable_on
_comp_deprecate_func _command_offset _comp_command_offset
_comp_deprecate_func _command _comp_command
_comp_deprecate_func _root_command _comp_root_command
_comp_deprecate_func _xfunc _comp_xfunc
_comp_deprecate_func _upvars _comp_upvars
_comp_deprecate_func __reassemble_comp_words_by_ref _comp__reassemble_words
_comp_deprecate_func __get_cword_at_cursor_by_ref _comp__get_cword_at_cursor
_comp_deprecate_func _get_comp_words_by_ref _comp_get_words
_comp_deprecate_func _longopt _comp_longopt
_comp_deprecate_func _split_longopt _comp__split_longopt
_comp_deprecate_func __ltrim_colon_completions _comp_ltrim_colon_completions

# Backwards compatibility for compat completions that use have().
# @deprecated should no longer be used; generally not needed with dynamically
#             loaded completions, and _comp_have_command is suitable for
#             runtime use.
# shellcheck disable=SC2317 # available at load time only
have()
{
    unset -v have
    _comp_have_command "$1" && have=yes
}

# This function shell-quotes the argument
# @deprecated Use `_comp_quote` instead.  Note that `_comp_quote` stores
#   the results in the variable `ret` instead of writing them to stdout.
quote()
{
    local quoted=${1//\'/\'\\\'\'}
    printf "'%s'" "$quoted"
}

# @deprecated Use `_comp_quote_compgen`
quote_readline()
{
    local ret
    _comp_quote_compgen "$1"
    printf %s "$ret"
} # quote_readline()

# This function is the same as `_comp_quote_compgen`, but receives the second
# argument specifying the variable name to store the result.
# @param $1  Argument to quote
# @param $2  Name of variable to return result to
# @deprecated Use `_comp_quote_compgen "$1"` instead.  Note that
# `_comp_quote_compgen` stores the result in a fixed variable `ret`.
_quote_readline_by_ref()
{
    [[ $2 == ret ]] || local ret
    _comp_quote_compgen "$1"
    [[ $2 == ret ]] || printf -v "$2" %s "$ret"
}

# This function shell-dequotes the argument
# @deprecated Use `_comp_dequote' instead.  Note that `_comp_dequote` stores
#   the results in the array `ret` instead of writing them to stdout.
dequote()
{
    local ret
    _comp_dequote "$1"
    local rc=$?
    printf %s "$ret"
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
# @deprecated  Use `_comp_upvars' instead
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
# @deprecated  Use `_comp_get_words cur' instead
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
} # _get_cword()

# Get word previous to the current word.
# This is a good alternative to `prev=${COMP_WORDS[COMP_CWORD-1]}' because bash4
# will properly return the previous word with respect to any given exclusions to
# COMP_WORDBREAKS.
# @deprecated  Use `_comp_get_words cur prev' instead
# @see _comp_get_words()
#
_get_pword()
{
    if ((COMP_CWORD >= 1)); then
        _get_cword "${@-}" 1
    fi
}

# Get real command.
# @deprecated Use `_comp_realcommand` instead.
# Note that `_comp_realcommand` stores the result in the variable `ret`
# instead of writing it to stdout.
_realcommand()
{
    local ret
    _comp_realcommand "$1"
    local rc=$?
    printf "%s\n" "$ret"
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
# @deprecated Use the new interface `_comp_initialize`.  The new interface
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

# @deprecated Use the variable `_comp_backup_glob` instead.  This is the
# backward-compatibility name.
# shellcheck disable=SC2154  # defined in the main "bash_completion"
_backup_glob=$_comp_backup_glob

# @deprecated use `_comp_cmd_cd` instead.
_cd()
{
    declare -F _comp_cmd_cd &>/dev/null || __load_completion cd
    _comp_cmd_cd "$@"
}

# ex: filetype=sh
