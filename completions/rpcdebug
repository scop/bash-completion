# bash completion for rpcdebug                             -*- shell-script -*-

_comp_cmd_rpcdebug__flags()
{
    local i module

    for ((i = 1; i < ${#words[@]}; i++)); do
        if [[ ${words[i]} == -m ]]; then
            module=${words[i + 1]-}
            break
        fi
    done

    if [[ $module ]]; then
        _comp_compgen_split -- "$(rpcdebug -vh 2>&1 |
            command sed -ne 's/^'"$module"'[[:space:]]\{1,\}//p')"
    fi
}

_comp_cmd_rpcdebug()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*s)
            _comp_cmd_rpcdebug__flags
            return
            ;;
        -*c)
            _comp_cmd_rpcdebug__flags
            return
            ;;
        -*m)
            _comp_compgen -- -W 'rpc nfs nfsd nlm'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- -h
        _comp_compgen -a -- -W '-s -c'
    fi
} &&
    complete -F _comp_cmd_rpcdebug rpcdebug

# ex: filetype=sh
