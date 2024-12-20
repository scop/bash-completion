# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd completion --write-to-stdout --shell bash".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" completion --write-to-stdout --shell bash 2>/dev/null)"

# ex: filetype=sh
