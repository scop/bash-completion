# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd install-completions". For example,
# some Go programs using https://github.com/WillAbides/kongplete do.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" install-completions 2>/dev/null)"

# ex: filetype=sh
