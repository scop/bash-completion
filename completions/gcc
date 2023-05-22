# gcc(1) completion                                        -*- shell-script -*-

_comp_cmd_gcc()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # Test that GCC is recent enough and if not fallback to
    # parsing of --completion option.
    if ! "$1" --completion=" " 2>/dev/null; then
        if [[ $cur == -* ]]; then
            local cc=$("$1" -print-prog-name=cc1 2>/dev/null)
            [[ $cc ]] || return
            _comp_compgen_split -- "$("$cc" --help 2>/dev/null | tr '\t' ' ' |
                command sed -e '/^  *-/!d' -e 's/ *-\([^][ <>]*\).*/-\1/')"
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        else
            _comp_compgen_filedir
        fi
        return
    fi

    local prev2 argument="" prefix prefix_length
    # extract also for situations like: -fsanitize=add
    if ((cword > 2)); then
        prev2="${COMP_WORDS[cword - 2]}"
    fi

    # sample: -fsan
    if [[ $cur == -* ]]; then
        argument=$cur
        prefix=""
    # sample: -fsanitize=
    elif [[ $cur == "=" && $prev == -* ]]; then
        argument=$prev$cur
        prefix=$prev$cur
    # sample: -fsanitize=add
    elif [[ $prev == "=" && $prev2 == -* ]]; then
        argument=$prev2$prev$cur
        prefix=$prev2$prev
    # sample: --param lto-
    elif [[ $prev == --param ]]; then
        argument="$prev $cur"
        prefix="$prev "
    fi

    if [[ ! $argument ]]; then
        _comp_compgen_filedir
    else
        # In situation like '-fsanitize=add' $cur is equal to last token.
        # Thus we need to strip the beginning of suggested option.
        prefix_length=$((${#prefix} + 1))
        local flags=$("$1" --completion="$argument" | cut -c $prefix_length-)
        [[ ${flags} == "=*" ]] && compopt -o nospace 2>/dev/null
        _comp_compgen -R -- -W "$flags"
    fi
} &&
    complete -F _comp_cmd_gcc gcc{,-5,-6,-7,-8} g++{,-5,-6,-7,-8} g77 g95 \
        gccgo{,-5,-6,-7,-8} gcj gfortran{,-5,-6,-7,-8} gpc &&
    _comp_cmd_gcc__setup_cmd()
    {
        local REPLY
        _comp_realcommand "$1"
        if [[ $REPLY == *$2* ]] ||
            "$1" --version 2>/dev/null | command grep -q GCC; then
            complete -F _comp_cmd_gcc "$1"
        else
            complete -F _comp_complete_minimal "$1"
        fi
    } &&
        _comp_cmd_gcc__setup_cmd cc gcc &&
        _comp_cmd_gcc__setup_cmd c++ g++ &&
        _comp_cmd_gcc__setup_cmd f77 gfortran &&
        _comp_cmd_gcc__setup_cmd f95 gfortran &&
        unset -f _comp_cmd_gcc__setup_cmd

# ex: filetype=sh
