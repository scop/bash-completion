# gkrellm(1) completion                                    -*- shell-script -*-

_comp_cmd_gkrellm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -t | --theme)
            _comp_compgen_filedir -d
            return
            ;;
        -p | --plugin)
            _comp_compgen_filedir so
            return
            ;;
        -s | --server)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        -l | --logfile)
            _comp_compgen_filedir
            return
            ;;
        -g | --geometry | -c | --config | -P | --port | -d | --debug-level)
            # Argument required but no completions available
            return
            ;;
        -h | --help | -v | --version)
            # All other options are noop with these
            return
            ;;
    esac

    _comp_compgen_help
} &&
    complete -F _comp_cmd_gkrellm gkrellm gkrellm2

# ex: filetype=sh
