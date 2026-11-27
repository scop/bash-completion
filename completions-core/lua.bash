# lua(1) completion

_comp_cmd_lua__filedir()
{
    # Match the whole filename, but replace only Readline's current word.
    local prefix=${cur%"${comp_args[1]}"}
    if [[ $prefix == *[:=] && $cur == "$prefix${comp_args[1]}" ]]; then
        _comp_compgen_filedir -f "$@" || return
        # Candidates are dequoted, so trim through the same delimiters.
        local pattern=${prefix//[!:=]/}
        pattern=${pattern//:/\*:}
        pattern=${pattern//=/\*=}
        # shellcheck disable=SC2295 # pattern is a glob
        COMPREPLY=("${COMPREPLY[@]#$pattern}")
    else
        _comp_compgen_filedir "$@"
    fi
}

_comp_cmd_lua()
{
    local cur prev words cword comp_args
    _comp_initialize -n := -- "$@" || return

    # After a script (or - for stdin), every remaining word is a script
    # argument, even if it starts with a dash.
    local i word=""
    for ((i = 1; i < cword; i++)); do
        word=${words[i]}
        # COMP_WORDS preserves quotes around a literal option.
        case $word in
            \"-*\" | \'-*\') word=${word:1:-1} ;;
        esac
        case $word in
            -[el])
                # Skip an operand supplied as a separate word.
                ((++i == cword)) && return
                ;;
            --)
                ((i + 1 == cword)) && break
                _comp_cmd_lua__filedir
                return
                ;;
            - | "" | [!-]*)
                _comp_cmd_lua__filedir
                return
                ;;
        esac
    done

    [[ $prev == -v ]] && return

    if [[ $word != -- && $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_cmd_lua__filedir 'l@(ua|?(ua)c)'
} &&
    complete -F _comp_cmd_lua lua{,5{,.}{0..4}}
