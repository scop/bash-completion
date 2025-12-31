#                                                          -*- shell-script -*-
# bash brogrammable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>

_comp_cmd_clisp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # completing an option (may or may not be separated by a space)
    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-h --help --version --license -B -K -M -m -L -N -E
            -q --quiet --silent -w -I -ansi -traditional -p -C -norc -i -c -l
            -o -x '
    else
        _comp_compgen_filedir
    fi

} &&
    complete -F _comp_cmd_clisp -o default clisp

# ex: filetype=sh
