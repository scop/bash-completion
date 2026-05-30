# lftpget(1) completion

_comp_cmd_lftpget()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-c -d -v'
    fi
} &&
    complete -F _comp_cmd_lftpget lftpget
