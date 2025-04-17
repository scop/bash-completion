# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd --print-own-completion bash".
# For example, https://github.com/iterative/shtab does.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" --print-own-completion bash 2>/dev/null)"

# ex: filetype=sh
