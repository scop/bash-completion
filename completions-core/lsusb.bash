# lsusb(8) completion

_comp_cmd_lsusb()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[sD]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}@([sD]|[hV]*))
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi
} &&
    complete -F _comp_cmd_lsusb lsusb
