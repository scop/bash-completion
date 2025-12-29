# iscsiadm(1) completion                                   -*- shell-script -*-

_comp_cmd_iscsiadm()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[motLU]*)'
    # shellcheck disable=SC2254
    case $prev in
        --mode | -${noargopts}m)
            _comp_compgen -- -W 'discovery node session iface fw host'
            return
            ;;
        --op | -${noargopts}o)
            _comp_compgen -- -W 'new delete update show'
            return
            ;;
        --type | -${noargopts}t)
            _comp_compgen -- -W 'sendtargets st slp isns fw'
            return
            ;;
        --loginall | --logoutall | -${noargopts}[LU])
            _comp_compgen -- -W 'all manual automatic'
            return
            ;;
    esac

    [[ $was_split ]] && return

    local options
    if ((cword > 1)); then

        case ${words[2]} in
            discovery)
                options='--help --version --debug --print --interface --type \
                    --portal --login --op --name --value'
                ;;
            node)
                options='--help --version --debug --print --loginall \
                    --logoutall--show  -T --portal --interface --login \
                    --logout --rescan --stats --op --name --value'
                ;;
            session)
                options='--help --version --debug --print --sid --logout \
                    --rescan --stats'
                ;;
            iface)
                options='--help --version --debug --print --interface --op \
                    --name --value'
                ;;
            fw)
                options='--login'
                ;;
            host)
                options='--print -H'
                ;;
        esac
    else
        options='--mode'
    fi

    _comp_compgen -- -W "$options"
} &&
    complete -F _comp_cmd_iscsiadm iscsiadm

# ex: filetype=sh
