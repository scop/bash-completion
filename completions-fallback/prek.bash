# 3rd party completion loader for commands emitting their completion using
# "COMPLETE=bash $cmd".
#
# This serves as a fallback in case the completion is not installed otherwise.

eval -- "$(COMPLETE=bash "$1" 2>/dev/null)"
