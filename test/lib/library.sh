# Bash library for bash-completion DejaGnu testsuite


# @param $1  Char to add to $COMP_WORDBREAKS
# @see remove_comp_wordbreak_char()
add_comp_wordbreak_char() {
    [[ "${COMP_WORDBREAKS//[^$1]}" ]] || COMP_WORDBREAKS+=$1
} # add_comp_wordbreak_char()


# Diff environment files to detect if environment is unmodified
# @param $1  File 1
# @param $2  File 2
# @param $3  Additional sed script
diff_env() {
    diff "$1" "$2" | sed -e "
# Remove diff line indicators
        /^[0-9,]\{1,\}[acd]/d
# Remove diff block separators
        /---/d
# Remove underscore variable
        /[<>] _=/d
# Remove PPID bash variable
        /[<>] PPID=/d
# Remove BASH_REMATCH bash variable
        /[<>] BASH_REMATCH=/d
        $3"
} # diff_env()


# Output array elements, sorted and separated by newline
# Unset variable after outputting.
# @param $1  Name of array variable to process
echo_array() {
    local name=$1[@]
    printf "%s\n" "${!name}" | sort
} # echo_array()


# Check if current bash version meets specified minimum
# @param $1  (integer) Major version number
# @param $2  (integer) Minor version number
# @param $3  (integer) Patch level
# @return  0 if success, > 0 if not
is_bash_version_minimal() {
    [[      (
                ${BASH_VERSINFO[0]} -gt $1
            ) || (
                ${BASH_VERSINFO[0]} -eq $1 &&
                ${BASH_VERSINFO[1]} -gt $2
            ) || (
                ${BASH_VERSINFO[0]} -eq $1 &&
                ${BASH_VERSINFO[1]} -eq $2 &&
                ${BASH_VERSINFO[2]} -ge $3
            )
    ]]
} # is_bash_version_minimal()


# @param $1  Char to remove from $COMP_WORDBREAKS
# @see add_comp_wordbreak_char()
remove_comp_wordbreak_char() {
    COMP_WORDBREAKS=${COMP_WORDBREAKS//$1}
} # remove_comp_wordbreak_char()


# Local variables:
# mode: shell-script
# sh-basic-offset: 4
# sh-indent-comment: t
# indent-tabs-mode: nil
# End:
# ex: ts=4 sw=4 et filetype=sh
