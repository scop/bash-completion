# $Id: bash_completion.sh,v 1.2 2006/02/25 01:21:33 ianmacd Exp $

# Check for bash (and that we haven't already been sourced).
[ -z "$BASH_VERSION" -o -n "$BASH_COMPLETION" ] && return

# Check for recent enough version of bash.
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}

# Check for interactive shell.
if [ -n "$PS1" ]; then
  if [ $bmajor -eq 2 -a $bminor '>' 04 ] || [ $bmajor -gt 2 ]; then
    if [ -r /etc/bash_completion ]; then
      # Source completion code.
      . /etc/bash_completion
    fi
  fi
fi
unset bash bminor bmajor
