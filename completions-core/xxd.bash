# xxd(1) completion                                        -*- shell-script -*-

_comp_cmd_xxd()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -help | -c | -cols | -g | -groupsize | -l | -len | -n | -name | \
            -o | -s | -seek | -v | -version)
            return
            ;;
        -R)
            _comp_compgen -- -W "always auto never"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_xxd xxd

# ex: filetype=sh
