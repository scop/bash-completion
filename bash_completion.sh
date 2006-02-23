# Check for bash (and that we haven't already been sourced).
[ -z "$BASH_VERSION" -o -n "$BASH_COMPLETION" ] && return

# Check for non-interactive shell.
[ -z "$PS1" ] && return

# Check for recent enough version of bash.
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ "$PS1" ] && [ $bmajor -eq 2 -a $bminor '>' 04 ] || [ $bmajor -gt 2 ]; then
  if [ -r /etc/bash_completion ]; then
    # Source completion code.
    . /etc/bash_completion
  fi
fi
unset bash bminor bmajor
