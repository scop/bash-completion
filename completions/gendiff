# gendiff(1) completion                                    -*- shell-script -*-

_comp_cmd_gendiff()
{
    local cur prev words cword comp_args
    _comp_initialize -o '@(diff|patch)' -- "$@" || return

    ((cword == 1)) && _comp_compgen_filedir -d
} &&
    complete -F _comp_cmd_gendiff gendiff

# ex: filetype=sh
