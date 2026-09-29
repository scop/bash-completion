# 3rd party completion loader for commands emitting their completion using
# "$cmd --bash-completion".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" --bash-completion 2>/dev/null)"
