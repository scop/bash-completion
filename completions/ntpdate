# bash completion for ntpdate                              -*- shell-script -*-

_comp_cmd_ntpdate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*k)
            _comp_compgen_filedir
            return
            ;;
        -*U)
            _comp_compgen -- -u
            return
            ;;
        -*p)
            _comp_compgen -- -W '{1..8}'
            return
            ;;

        -*[aeot])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h || _comp_compgen_usage
    else
        _comp_compgen_known_hosts -- "$cur"
    fi
} &&
    complete -F _comp_cmd_ntpdate ntpdate

# ex: filetype=sh
