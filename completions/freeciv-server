# freeciv-server completion                                -*- shell-script -*-

_comp_cmd_civserver()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -f | -g | -l | -r | --file | --log | --gamelog | --read)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi

} &&
    complete -F _comp_cmd_civserver civserver freeciv-server

# ex: filetype=sh
