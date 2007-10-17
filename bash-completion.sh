if [ "$PS1" ] && [ -f /etc/bash_completion ]; then
  if [ ! -z "$SHELL" ] && [ "bash" == "${SHELL##*/}" ]; then
    bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
    if [ "$bmajor" -eq 2 ] && [ "$bminor" -gt 04 ] || [ "$bmajor" -gt 2 ]; then	# interactive shell
      # Source completion code
      . /etc/bash_completion
    fi
    unset bash bmajor bminor
  fi
fi
