# Bash library for bash-completion DejaGnu testsuite


# Diff environment files to detect if environment is unmodified
# @param $1  File 1
# @param $2  File 2
# @param $1  Additional sed script
diff_env() {
	diff "$1" "$2" | sed -e "
	/^[0-9,]\+[acd]/d  # Remove diff line indicators
	/---/d            # Remove diff block separators
	/[<>] _=/d        # Remove underscore variable
	/[<>] PPID=/d     # Remove PPID bash variable
	$3"
} # diff_env()


# Output array elements, sorted and separated by newline
# Unset variable after outputting.
# @param $1  Name of array variable to process
echo_array() {
	local IFS=$'\n'
	eval printf "%s" \"\${$1[*]}\" | sort
}


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

# Local variables:
# mode: shell-script
# sh-basic-offset: 4
# sh-indent-comment: t
# indent-tabs-mode: nil
# End:
# ex: ts=4 sw=4 et filetype=sh
