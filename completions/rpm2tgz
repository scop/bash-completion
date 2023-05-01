# Slackware rpm2tgz completion                             -*- shell-script -*-

_comp_cmd_rpm2tgz()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-s -S -n -r -d -c'
        return
    fi

    _comp_compgen_filedir "rpm"
} &&
    complete -F _comp_cmd_rpm2tgz rpm2tgz rpm2txz rpm2targz

# ex: filetype=sh
