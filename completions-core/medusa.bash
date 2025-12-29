# bash completion for medusa                               -*- shell-script -*-

_comp_cmd_medusa()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -*[HUPCO])
            _comp_compgen_filedir
            return
            ;;
        -*M)
            _comp_compgen_split -- "$("$1" -d | _comp_awk '/^ +\+/ {print $2}' |
                command sed -e 's/\.mod$//')"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_medusa medusa

# ex: filetype=sh
