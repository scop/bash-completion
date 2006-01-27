bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ "$PS1" ] && [ "$bmajor" -eq 2 ] && [ "$bminor" '>' 04 ] || [ $bmajor -gt 2 ] \
	&& [ -f /etc/bash_completion ]; then	# interactive shell
	# Source completion code
	. /etc/bash_completion
fi
unset bash bmajor bminor
