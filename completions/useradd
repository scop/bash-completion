# useradd(8) completion                                    -*- shell-script -*-

_comp_cmd_useradd()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    # TODO: if -o/--non-unique is given, could complete on existing uids
    #       with -u/--uid

    local word chroot="" has_chroot=""
    for word in "${words[@]}"; do
        if [[ $has_chroot ]]; then
            chroot=$word
            break
        fi
        [[ $word != -@(R|-root) ]] || has_chroot=set
    done

    local noargopts='!(-*|*[cefKpubdkRgGZs]*)'
    # shellcheck disable=SC2254
    case $prev in
        --comment | --help | --expiredate | --inactive | --key | --password | \
            --uid | -${noargopts}[chefKpu])
            return
            ;;
        --base-dir | --home-dir | --skel | --root | -${noargopts}[bdkR])
            _comp_compgen_filedir -d
            return
            ;;
        --gid | -${noargopts}g)
            _comp_compgen_gids
            _comp_compgen -a -- -g
            return
            ;;
        --groups | -${noargopts}G)
            _comp_delimited , -g
            return
            ;;
        --selinux-user | -${noargopts}Z)
            _comp_compgen_selinux_users
            return
            ;;
        --shell | -${noargopts}s)
            _comp_compgen_shells "${chroot-}"
            return
            ;;
    esac

    [[ $was_split ]] && return

    [[ $cur == -* ]] &&
        _comp_compgen_help
} &&
    complete -F _comp_cmd_useradd useradd

# ex: filetype=sh
