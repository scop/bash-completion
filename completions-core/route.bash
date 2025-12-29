# Linux route(8) completion                                -*- shell-script -*-

[[ $OSTYPE == *linux* ]] || return 1

_comp_cmd_route()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $prev == dev ]]; then
        _comp_compgen_available_interfaces
        return
    fi

    # Remove already given options from completions
    local opt found i
    for opt in add del -host -net netmask metric mss window irtt reject mod \
        dyn reinstate dev default gw; do
        found=""
        for ((i = 1; i < cword; i++)); do
            [[ ${words[i]} == "$opt" ]] && found=set && break
        done
        [[ $found ]] || COMPREPLY+=("$opt")
    done

    ((${#COMPREPLY[@]})) &&
        _comp_compgen -- -W '"${COMPREPLY[@]}"'
} &&
    complete -F _comp_cmd_route route

# ex: filetype=sh
