# bash brogrammable completion for various Common Lisp implementations by
# Nikodemus Siivola <nikodemus@random-state.net>
#
# $Id: clisp,v 1.2 2004/03/30 23:05:45 ianmacd Exp $

_clisp()
{
    local cur

    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}

    # completing an option (may or may not be separated by a space)
    if [[ "$cur" == -* ]]; then
	COMPREPLY=( $( compgen -W '-h --help --version --license -B -K \
                     -M -m -L -N -E -q --quiet --silent -w -I -ansi \
                     -traditional -p -C -norc -i -c -l -o -x ' \
                     -- $cur ) )
    else
	_filedir
    fi

    return 0
}
complete -F _clisp -o default clisp
