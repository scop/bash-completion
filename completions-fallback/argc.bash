# 3rd party completion loader for commands emitting their completion using
# "$cmd --argc-completions bash".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" --argc-completions bash 2>/dev/null)"
