# autorpm(8) completion

_comp_cmd_autorpm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    _comp_compgen -- -W '--notty --debug --help --version auto add fullinfo
        info help install list remove set'

} &&
    complete -F _comp_cmd_autorpm autorpm
