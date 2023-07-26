# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd --print-completion bash".
# For example, many Python programs using https://github.com/iterative/shtab do.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" --print-completion bash 2>/dev/null)"

# ex: filetype=sh
