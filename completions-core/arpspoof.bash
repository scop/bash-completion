# arpspoof completion                                      -*- shell-script -*-

_comp_cmd_arpspoof()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -i)
            _comp_compgen_available_interfaces -a
            return
            ;;
        -t)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
    else
        _comp_compgen_known_hosts -- "$cur"
    fi

} &&
    complete -F _comp_cmd_arpspoof arpspoof

# ex: filetype=sh
