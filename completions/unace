# unace(1) completion                                      -*- shell-script -*-

_comp_cmd_unace()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-c -c- -f -f- -o -o- -p -y -y-'
    else
        if ((cword == 1)); then
            _comp_compgen -- -W 'e l t v x'
        else
            _comp_compgen_filedir '@(ace|cba)'
        fi
    fi
} &&
    complete -F _comp_cmd_unace unace

# ex: filetype=sh
