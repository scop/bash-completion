# 3rd party completion loader for commands supporting their use
# as a `complete -C` handler.
#
# This serves as a fallback in case the completion is not installed otherwise.

type "$1" &>/dev/null && complete -C "\"$1\" 2>/dev/null" "$1"
