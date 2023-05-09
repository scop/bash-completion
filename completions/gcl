#                                                          -*- shell-script -*-
# bash programmable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>

_comp_cmd_gcl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # completing an option (may or may not be separated by a space)
    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-eval -load -f -batch -dir -libdir -compile
            -o-file -c-file -h-file -data-file -system-p'
    else
        _comp_compgen_filedir
    fi

} &&
    complete -F _comp_cmd_gcl -o default gcl

# ex: filetype=sh
