# dmypy completion                                         -*- shell-script -*-

_comp_cmd_dmypy()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version | -[hV])
            return
            ;;
        --status-file)
            _comp_compgen_filedir
            return
            ;;
    esac

    local cmd="" has_cmd="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} != -* && ${words[i - 1]} != --status-file ]]; then
            cmd=${words[i]}
            has_cmd=set
            break
        fi
    done

    case ${cmd-} in
        check | run)
            _comp_compgen_filedir '@(py|pyi)'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    if [[ ! $has_cmd ]]; then
        local cmds=$("$1" --help 2>&1 |
            command sed -ne '/positional arguments/{p;n;p;q;}' |
            command sed -ne 's/{\(.*\)}/\1/p')
        _comp_compgen -F , -- -W '$cmds'
        return
    fi
} &&
    complete -F _comp_cmd_dmypy dmypy

# ex: filetype=sh
