# mailman qrunner completion                               -*- shell-script -*-

_comp_cmd_qrunner()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--runner --once --list --verbose --subproc --help'
    fi

} &&
    complete -F _comp_cmd_qrunner qrunner

# ex: filetype=sh
