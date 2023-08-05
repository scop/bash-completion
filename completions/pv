# pv(1) completion                                         -*- shell-script -*-

_comp_cmd_pv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[VAFDiwHNLBRPd]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --last-written | --format | --delay-start | \
            --interval | --width | --height | --name | --rate-limit | \
            --buffer-size | -${noargopts}[hVAFDiwHNLB])
            return
            ;;
        --remote | -${noargopts}R)
            _comp_compgen_pids
            return
            ;;
        --pidfile | --watchfd | -${noargopts}[Pd])
            _comp_compgen_filedir pid
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_pv pv

# ex: filetype=sh
