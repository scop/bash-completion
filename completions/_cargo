# 3rd party completion loader for cargo                    -*- shell-script -*-
#
# This serves as a fallback in case the completion is not installed otherwise.

# shellcheck disable=SC2168 # "local" is ok, assume sourced by _comp_load
local rustup="${1%cargo}rustup" # use rustup from same dir
eval -- "$("$rustup" completions bash cargo 2>/dev/null)"

# ex: filetype=sh
