# mailman config_list completion                           -*- shell-script -*-

_comp_cmd_config_list()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        -i | -o | --inputfile | --outputfile)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--inputfile --outputfile --checkonly
            --verbose --help'
    else
        # Prefer `list_lists` in the same dir as command
        local pathcmd
        pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
        _comp_xfunc list_lists mailman_lists
    fi

} &&
    complete -F _comp_cmd_config_list config_list

# ex: filetype=sh
