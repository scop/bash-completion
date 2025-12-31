# sqlite3(1) completion                                    -*- shell-script -*-

_comp_cmd_sqlite3()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local dbexts='@(sqlite?(3)|?(s?(3))db)'

    case $prev in
        -help | -version | -lookaside | -maxsize | -mmap | -newline | \
            -nullvalue | -pagecache | -scratch | -separator | -vfs | *.$dbexts)
            return
            ;;
        -init)
            _comp_compgen_filedir
            return
            ;;
        -cmd)
            _comp_compgen_commands
            return
            ;;
    esac

    [[ $cword -gt 2 && ${words[cword - 2]} == -@(lookaside|pagecache|scratch) ]] &&
        return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        return
    fi

    _comp_compgen_filedir "$dbexts"
} &&
    complete -F _comp_cmd_sqlite3 sqlite3

# ex: filetype=sh
