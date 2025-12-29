# file(1) completion                                       -*- shell-script -*-

_comp_cmd_file()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[Fmfe]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --separator | -${noargopts}[vF])
            return
            ;;
        --magic-file | --files-from | -${noargopts}[mf])
            _comp_compgen_filedir
            return
            ;;
        --exclude | -${noargopts}e)
            _comp_compgen -- -W 'apptype ascii cdf compress elf encoding soft
                tar text tokens troff'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_file file

# ex: filetype=sh
