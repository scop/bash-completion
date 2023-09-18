# 3rd party completion loader for commands emitting        -*- shell-script -*-
# their completion using "_${cmdname^^}_COMPLETE=source $cmd".
# This pattern is very similar to `completions/_pipenv`, but the value of the
# environment variable is slightly different.
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$(
    # shellcheck disable=SC2154
    ucname="${cmdname^^}"
    ucname=${ucname//-/_}
    export "_${ucname}_COMPLETE=source"
    "$1" 2>/dev/null
)"

# ex: filetype=sh
