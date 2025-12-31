# 3rd party completion loader for kontena                  -*- shell-script -*-
#
# This serves as a fallback in case the completion is not installed otherwise.

# To avoid sourcing an empty string with `. "$(...)"` on failing to obtain the
# path, we assign the output to a variable `_comp_cmd_kontena__completion_path`
# and test it before sourcing.  The variable is removed on successful loading
# but left on a failure for the debugging purpose.
_comp_cmd_kontena__completion_path=$("$1" whoami --bash-completion-path 2>/dev/null) &&
    [[ -r $_comp_cmd_kontena__completion_path ]] &&
    . "$_comp_cmd_kontena__completion_path" &&
    unset -v _comp_cmd_kontena__completion_path

# ex: filetype=sh
