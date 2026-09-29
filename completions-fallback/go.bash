# 3rd party completion loader for go
#
# This serves as a fallback in case the completion is not installed otherwise.

# shellcheck disable=SC2168 # "local" is ok, assume sourced by _comp_load
local completer
for completer in {"${1%"${1##*/}"}","${GOBIN-/__Dummy__}/","${GOPATH-/__Dummy__}/bin/",}gocomplete; do
    if type "$completer" &>/dev/null; then
        complete -C "\"$completer\" 2>/dev/null" "$1"
        break
    fi
done
