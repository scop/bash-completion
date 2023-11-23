# bash completion for cvsps                                -*- shell-script -*-

_comp_cmd_cvsps()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -h | -z | -f | -d | -l | --diff-opts | --debuglvl)
            return
            ;;
        -s)
            _comp_compgen_split -- "$("$1" 2>/dev/null |
                _comp_awk '/^PatchSet:?[ \t]/ { print $2 }')"
            return
            ;;
        -a)
            _comp_compgen_split -- "$("$1" 2>/dev/null |
                _comp_awk '/^Author:[ \t]/ { print $2 }')"
            return
            ;;
        -b)
            _comp_compgen_split -- "$("$1" 2>/dev/null |
                _comp_awk '/^Branch:[ \t]/ { print $2 }')"
            return
            ;;
        -r)
            _comp_compgen_split -- "$("$1" 2>/dev/null |
                _comp_awk '/^Tag:[ \t]+[^(]/ { print $2 }')"
            return
            ;;
        -p)
            _comp_compgen_filedir -d
            return
            ;;
        --test-log)
            _comp_compgen_filedir
            return
            ;;
        -Z)
            _comp_compgen -- -W '{1..9}'
            return
            ;;
        --root)
            _comp_compgen -x cvs roots
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
    else
        _comp_compgen -x cvs roots
    fi
} &&
    complete -F _comp_cmd_cvsps cvsps

# ex: filetype=sh
