# bash declare completion                                  -*- shell-script -*-

_comp_cmd_declare()
{
    local cur prev words cword comp_args
    _comp_initialize -n := -- "$@" || return

    if [[ $cur == [-+]* ]]; then
        local opts
        _comp_compgen -Rv opts usage -c help -s "$1"
        # Most options also have a '+' form.
        # We'll exclude the ones that don't with compgen.
        opts+=("${opts[@]/-/+}")
        _comp_compgen -- -W "${opts[*]}" -X '+[Ffgp]'
        return
    fi

    local i=1
    while [[ ${words[i]} == [-+]* ]]; do
        case ${words[i]} in
            -*[aA]*)
                _comp_compgen -- -A arrayvar
                return
                ;;
            -*[fF]*)
                _comp_compgen -- -A function
                return
                ;;
        esac
        ((i++))
    done
    if ((i > 1)); then
        # There was at least one option and it was not one that limited
        # operations to functions and array variables
        _comp_variable_assignments "$cur" && return
        _comp_compgen -- -A variable
    fi
} &&
    complete -F _comp_cmd_declare declare typeset

# ex: filetype=sh
