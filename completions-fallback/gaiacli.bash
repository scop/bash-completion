# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd completion".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" completion 2>/dev/null)"

# ex: filetype=sh
