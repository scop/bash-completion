# bash programmable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>
#
# $Id: sbcl,v 1.2 2004/03/30 23:05:45 ianmacd Exp $

_sbcl()
{
    local cur

    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}

    # completing an option (may or may not be separated by a space)
    if [[ "$cur" == -* ]]; then
	COMPREPLY=( $( compgen -W '--core --noinform --help --version \
                     --sysinit --userinit --eval --noprint --disable-debugger \
                     --end-runtime-options --end-toplevel-options ' -- $cur ) )
    else
	_filedir
    fi

    return 0
}
complete -F _sbcl -o default sbcl sbcl-mt
