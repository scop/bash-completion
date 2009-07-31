# -*- mode: shell-script; sh-basic-offset: 8; indent-tabs-mode: t -*-
# ex: ts=8 sw=8 noet filetype=sh
#
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
# @param $1  Name of array variable to process
echo_array() {
	local IFS=$'\n'
	eval echo \"\${$1[*]}\" | sort
}
