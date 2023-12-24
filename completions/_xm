# bash completion for xm                                   -*- shell-script -*-

# Use of this file is deprecated.  The 'xm' command itself is no longer
# provided by upstream.  It has been replaced with the 'xl' command, for
# which upstream provides completion, use that instead.

_comp_cmd_xm__domain_names()
{
    _comp_compgen_split -- "$(xm list 2>/dev/null |
        _comp_awk '!/Name|Domain-0/ { print $1 }')"
}

_comp_cmd_xm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    # TODO: split longopt

    local REPLY command commands options

    commands='console vncviewer create new delete destroy domid domname
        dump-core list mem-max mem-set migrate pause reboot rename reset
        restore resume save shutdown start suspend sysrq trigger top unpause
        uptime usb-add usb-del vcpu-list vcpu-pin vcpu-set debug-keys dmesg
        info log serve sched-credit sched-sedf block-attach block-detach
        block-list block-configure network-attach network-detach network-list
        vtpm-list pci-attach pci-detach pci-list pci-list-assignable-devices
        scsi-attach scsi-detach scsi-list vnet-list vnet-create vnet-delete
        labels addlabel rmlabel getlabel dry-run resources dumppolicy setpolicy
        resetpolicy getpolicy shell help'

    if ((cword == 1)); then
        _comp_compgen -- -W "$commands"
    else
        if [[ $cur == *=* ]]; then
            prev=${cur/=*/}
            cur=${cur/*=/}
        fi

        command=${words[1]}
        if [[ $cur == -* ]]; then
            # possible options for the command
            case $command in
                create)
                    options='-c'
                    ;;
                dmesg)
                    options='--clear'
                    ;;
                list)
                    options='--long'
                    ;;
                reboot)
                    options='-w -a'
                    ;;
                shutdown)
                    options='-w -a -R -H'
                    ;;
                sched-credit)
                    options='-d -w -c'
                    ;;
                block-list | network-list | vtpm-list | vnet-list)
                    options='-l --long'
                    ;;
                getpolicy)
                    options='--dumpxml'
                    ;;
                new)
                    options='-h --help --help_config -q --quiet --path= -f=
                        --defconfig= -F= --config= -b --dryrun -x --xmldryrun
                        -s --skipdtd -p --paused -c --console_autoconnect'
                    ;;
            esac
            _comp_compgen -- -W "$options"
        else
            case $command in
                console | destroy | domname | domid | list | mem-set | \
                    mem-max | pause | reboot | rename | shutdown | unpause | \
                    vcpu-list | vcpu-pin | vcpu-set | block-list | \
                    network-list | vtpm-list)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                    esac
                    ;;
                migrate)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen_known_hosts -- "$cur"
                            ;;
                    esac
                    ;;
                restore | dry-run | vnet-create)
                    _comp_compgen_filedir
                    ;;
                save)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen_filedir
                            ;;
                    esac
                    ;;
                sysrq)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen -- -W "r s e i u b"
                            ;;
                    esac
                    ;;
                block-attach)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen -- -W "phy: file:"
                            ;;
                        5)
                            _comp_compgen -- -W "w r"
                            ;;
                        6)
                            _comp_cmd_xm__domain_names
                            ;;
                    esac
                    ;;
                block-detach)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen_split -- "$(xm block-list "$prev" \
                                2>/dev/null | _comp_awk '!/Vdev/ { print $1 }')"
                            ;;
                    esac
                    ;;
                network-attach)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        *)
                            _comp_compgen -- -W "script= ip= mac= bridge=
                                backend="
                            ;;
                    esac
                    ;;
                network-detach)
                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                        3)
                            _comp_compgen_split -- "$(xm network-list "$prev" \
                                2>/dev/null | _comp_awk '!/Idx/ { print $1 }')"
                            ;;
                    esac
                    ;;
                sched-credit)
                    case $prev in
                        -d)
                            _comp_cmd_xm__domain_names
                            return
                            ;;
                    esac
                    ;;
                create)
                    _comp_compgen_filedir
                    _comp_compgen -a split -- "$(
                        command ls /etc/xen 2>/dev/null
                    )"
                    ;;
                new)
                    case $prev in
                        -f | -F | --defconfig | --config)
                            _comp_compgen_filedir
                            return
                            ;;
                        --path)
                            _comp_compgen_filedir -d
                            return
                            ;;
                    esac

                    _comp_count_args
                    case $REPLY in
                        2)
                            _comp_cmd_xm__domain_names
                            ;;
                    esac
                    ;;
            esac
        fi
    fi
} &&
    complete -F _comp_cmd_xm xm

# ex: filetype=sh
