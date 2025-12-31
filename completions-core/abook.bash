# abook(1) completion                                      -*- shell-script -*-

_comp_cmd_abook()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # abook only takes options, tabbing after command name adds a single dash
    [[ $cword -eq 1 && ! $cur ]] &&
        {
            compopt -o nospace
            COMPREPLY=("-")
            return
        }

    case $cur in
        -*)
            _comp_complete_longopt "$@"
            return
            ;;
    esac

    case $prev in
        --informat)
            _comp_compgen_split -- "$("$1" --formats |
                command sed -n -e 's/^'$'\t''\([a-z]*\).*/\1/p' -e '/^$/q')"
            ;;
        --outformat)
            _comp_compgen_split -- "$("$1" --formats |
                command sed -n -e '/^$/,$s/^'$'\t''\([a-z]*\).*/\1/p')"
            ;;
        --infile)
            _comp_compgen -- -W stdin
            _comp_compgen -a filedir
            ;;
        --outfile)
            _comp_compgen -- -W stdout
            _comp_compgen -a filedir
            ;;
        --config | --datafile)
            _comp_compgen_filedir
            ;;
    esac
} &&
    complete -F _comp_cmd_abook abook

# ex: filetype=sh
