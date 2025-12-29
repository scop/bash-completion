# mailman cleanarch completion                             -*- shell-script -*-

_comp_cmd_cleanarch()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--status --dry-run --quiet --help'
    fi

} &&
    complete -F _comp_cmd_cleanarch cleanarch

# ex: filetype=sh
