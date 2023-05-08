# mailman mmsitepass completion                            -*- shell-script -*-

_comp_cmd_mmsitepass()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--listcreator --help'
    fi

} &&
    complete -F _comp_cmd_mmsitepass mmsitepass

# ex: filetype=sh
