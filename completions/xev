# xev(1) completion                                        -*- shell-script -*-

_comp_cmd_xev()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -display | -geometry | -bw | -id | -name)
            return
            ;;
        -bs)
            _comp_compgen -- -W 'NotUseful WhenMapped Always'
            return
            ;;
        -event)
            _comp_compgen -- -W 'keyboard mouse expose visibility structure
                substructure focus property colormap owner_grab_button randr
                button'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi
} &&
    complete -F _comp_cmd_xev xev

# ex: filetype=sh
