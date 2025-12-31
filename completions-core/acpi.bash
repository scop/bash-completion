# acpi(1) completion                                       -*- shell-script -*-

_comp_cmd_acpi()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[d]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[hv])
            return
            ;;
        --directory | -${noargopts}d)
            _comp_compgen_filedir -d
            return
            ;;
    esac

    _comp_compgen_help
} &&
    complete -F _comp_cmd_acpi acpi

# ex: filetype=sh
