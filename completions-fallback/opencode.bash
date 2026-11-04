# 3rd party completion loader for opencode.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$(
    "$1" --completions bash 2>/dev/null || # v2
        "$1" completion 2>/dev/null        # v1
)"
