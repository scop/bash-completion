# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd install-completions".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" install-completions 2>/dev/null)"

# ex: filetype=sh
