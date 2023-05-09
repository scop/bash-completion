# unrar(1) completion                                      -*- shell-script -*-

_comp_cmd_unrar()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-ad -ap -av- -c- -cfg- -cl -cu -dh -ep -f -idp
            -ierr -inul -kb -o+ -o- -ow -p -p- -r -ta -tb -tn -to -u -v -ver
            -vp -x -x@ -y'
    else
        if ((cword == 1)); then
            _comp_compgen -- -W 'e l lb lt p t v vb vt x'
        else
            _comp_compgen_filedir '@(rar|exe|cbr)'
        fi
    fi

} &&
    complete -F _comp_cmd_unrar unrar

# ex: filetype=sh
