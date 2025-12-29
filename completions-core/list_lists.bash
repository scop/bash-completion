# mailman list_lists completion                            -*- shell-script -*-

# @since 2.12
_comp_xfunc_list_lists_compgen_mailman_lists()
{
    _comp_compgen_split -- "$(list_lists -b 2>/dev/null)"
}

_comp_deprecate_func 2.12 _mailman_lists \
    _comp_xfunc_list_lists_compgen_mailman_lists

_comp_cmd_list_lists()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--advertised --virtual-host-overview --bare
            --help'
    fi

} &&
    complete -F _comp_cmd_list_lists list_lists

# ex: filetype=sh
