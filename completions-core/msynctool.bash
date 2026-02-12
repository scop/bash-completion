# bash completion for msynctool                            -*- shell-script -*-

_comp_cmd_msynctool()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $words in
        --configure)
            _comp_compgen_split -- "$("$1" --showgroup "$prev" |
                _comp_awk '/^Member/ {print $2}' | command sed -e 's/:$//')"
            return
            ;;
        --addmember)
            _comp_compgen_split -- "$("$1" --listplugins | _comp_tail -n +2)"
            return
            ;;
    esac

    case $prev in
        --configure | --addgroup | --delgroup | --showgroup | --sync | --addmember)
            _comp_compgen_split -- "$("$1" --listgroups | _comp_tail -n +2)"
            return
            ;;
        --showformats | --filter-objtype | --slow-sync)
            _comp_compgen_split -- "$("$1" --listobjects | _comp_tail -n +2)"
            return
            ;;
    esac

    _comp_compgen -- -W '--listgroups --listplugins --listobjects --showformats
        --showgroup --sync --filter-objtype --slow-sync --wait --multi
        --addgroup --delgroup --addmember --configure --manual --configdir
        --conflict'
} &&
    complete -F _comp_cmd_msynctool msynctool

# ex: filetype=sh
