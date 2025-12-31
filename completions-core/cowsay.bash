# bash completion for cowsay                               -*- shell-script -*-

_comp_cmd_cowsay()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -f)
            _comp_compgen_split -- "$(cowsay -l 2>/dev/null | tail -n +2)"
            return
            ;;
    esac

    # relevant options completion
    _comp_compgen -- -W '-b -d -g -p -s -t -w -y -e -f -h -l -n -T -W'

} &&
    complete -F _comp_cmd_cowsay -o default cowsay cowthink

# ex: filetype=sh
