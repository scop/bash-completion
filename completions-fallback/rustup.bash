# 3rd party completion loader for rustup                   -*- shell-script -*-
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$("$1" completions bash rustup 2>/dev/null)"

# ex: filetype=sh
