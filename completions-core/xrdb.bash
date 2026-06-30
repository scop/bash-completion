# xrdb(1) completion

_comp_cmd_xrdb()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -backup | -display | -get | -help)
            return
            ;;
        -cpp | -edit)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_compgen -- -W '"${COMPREPLY[@]}" -D -I -U' -X -Dname &&
            [[ $COMPREPLY == -[DIU] ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_xrdb xrdb
