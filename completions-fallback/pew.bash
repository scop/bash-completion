# 3rd party completion loader for pew
#
# This serves as a fallback in case the completion is not installed otherwise.

# shellcheck disable=SC2168 # "local" is ok, assume sourced by _comp_load
local PS1 # This is to prevent pew's shell_config/init.bash to modify PS1.
eval -- "$("$1" shell_config 2>/dev/null)"
