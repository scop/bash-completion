# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd generate-completions bash".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" generate-completions bash 2>/dev/null)"

# ex: filetype=sh
