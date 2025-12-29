#                                                          -*- shell-script -*-
# bash programmable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>

_comp_cmd_lisp()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # completing an option (may or may not be separated by a space)
    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-core -lib -batch -quit -edit -eval -init
            -dynamic-space-size -hinit -noinit -nositeinit -load -slave'
    else
        _comp_compgen_filedir
    fi

} &&
    complete -F _comp_cmd_lisp -o default lisp

# ex: filetype=sh
