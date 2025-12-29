# ecryptfs-migrate-home(8) completion                      -*- shell-script -*-

_comp_cmd_ecryptfs_migrate_home()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help)
            return
            ;;
        --user | -u)
            _comp_compgen -- -u
            return
            ;;
    esac

    _comp_compgen_help
} &&
    complete -F _comp_cmd_ecryptfs_migrate_home ecryptfs-migrate-home

# ex: filetype=sh
