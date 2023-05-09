#                                                          -*- shell-script -*-
# bash programmable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>

_comp_cmd_sbcl()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # completing an option (may or may not be separated by a space)
    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--core --noinform --help --version --sysinit
            --userinit --eval --noprint --disable-debugger
            --end-runtime-options --end-toplevel-options'
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_sbcl sbcl sbcl-mt

# ex: filetype=sh
