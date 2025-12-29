# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "$cmd completion bash".
# For example, many Go programs using https://github.com/spf13/cobra do.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" completion bash 2>/dev/null)"

# ex: filetype=sh
