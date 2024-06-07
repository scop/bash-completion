# 3rd party completion loader for commands using           -*- shell-script -*-
# version 1 of the https://cli.urfave.org library.
#
# This serves as a fallback in case the completion is not installed otherwise.

# https://github.com/urfave/cli/blob/v1-maint/docs/v1/manual.md#bash-completion
# https://github.com/urfave/cli/blob/v1-maint/autocomplete/bash_autocomplete
_comp_cmd__urfave_cli_v1()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local compcmd=("${words[@]:0:cword}")
    if [[ $cur == -* ]]; then
        compcmd+=("$cur")
    fi
    compcmd+=(--generate-bash-completion)

    _comp_compgen_split -- "$("${compcmd[@]}" 2>/dev/null)"
} &&
    complete -o bashdefault -o default -o nospace \
        -F _comp_cmd__urfave_cli_v1 "$1"

# ex: filetype=sh
