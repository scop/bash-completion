# chsh(1) completion                                       -*- shell-script -*-

# Use of this file is deprecated on Linux systems whose chsh is from
# util-linux. Upstream completion is in util-linux >= 2.23, use that instead.

_comp_cmd_chsh()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local word chroot="" has_chroot=""
    for word in "${words[@]}"; do
        if [[ $has_chroot ]]; then
            chroot=$word
            break
        fi
        [[ $word != -@(R|-root) ]] || has_chroot=set
    done

    case $prev in
        --list-shells | --help | -v | --version)
            return
            ;;
        -R | --root)
            _comp_compgen_filedir -d
            return
            ;;
        -s | --shell)
            _comp_compgen_shells "${chroot-}"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
    else
        _comp_compgen_allowed_users
    fi

} &&
    complete -F _comp_cmd_chsh chsh

# ex: filetype=sh
