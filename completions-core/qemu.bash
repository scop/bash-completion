# bash completion for qemu                                 -*- shell-script -*-

_comp_cmd_qemu()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -fd[ab] | -hd[abcd] | -cdrom | -option-rom | -kernel | -initrd | \
            -bootp | -pidfile | -loadvm | -mtdblock | -sd | -pflash | -bios)
            _comp_compgen_filedir
            return
            ;;
        -tftp | -smb | -L | -chroot)
            _comp_compgen_filedir -d
            return
            ;;
        -boot)
            _comp_compgen -- -W 'a c d n'
            return
            ;;
        -k)
            local -a keymaps
            _comp_expand_glob keymaps '/usr/{local/,}share/qemu/keymaps/!(common|modifiers)' &&
                _comp_compgen -- -W '"${keymaps[@]##*/}"'
            return
            ;;
        -soundhw)
            _comp_compgen_split -- "$("$1" -soundhw help | _comp_awk '
                function islower(s) { return length(s) > 0 && s == tolower(s); }
                islower(substr($0, 1, 1)) {print $1}') all"
            return
            ;;
        -machine | -M)
            _comp_compgen_split -- "$("$1" "$prev" help | _comp_awk '
                function islower(s) { return length(s) > 0 && s == tolower(s); }
                islower(substr($0, 1, 1)) {print $1}')"
            return
            ;;
        -cpu)
            _comp_compgen_split -- "$("$1" -cpu help | _comp_awk '{print $2}')"
            return
            ;;
        -usbdevice)
            _comp_compgen -- -W 'mouse tablet disk: host: serial: braille net'
            return
            ;;
        -net)
            _comp_compgen -- -W 'nic user tap socket vde none dump'
            return
            ;;
        -serial | -parallel | -monitor)
            _comp_compgen -- -W 'vc pty none null /dev/ file: stdio pipe: COM
                udp: tcp: telnet: unix: mon: braille'
            return
            ;;
        -redir)
            _comp_compgen -- -S":" -W 'tcp udp'
            return
            ;;
        -bt)
            _comp_compgen -- -W 'hci vhci device'
            return
            ;;
        -vga)
            _comp_compgen -- -W 'cirrus std vmware xenfb none'
            return
            ;;
        -drive)
            _comp_compgen -- -S"=" -W 'file if bus unit index media cyls
                snapshot cache format serial addr'
            return
            ;;
        -balloon)
            _comp_compgen -- -W 'none virtio'
            return
            ;;
        -smbios)
            _comp_compgen -- -W 'file type'
            return
            ;;
        -watchdog)
            _comp_compgen_split -- "$("$1" -watchdog help 2>&1 |
                _comp_awk '{print $1}')"
            return
            ;;
        -watchdog-action)
            _comp_compgen -- -W 'reset shutdown poweroff pause debug none'
            return
            ;;
        -runas)
            _comp_compgen_allowed_users
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
        _comp_compgen -a -- -W '-fd{a,b} -hd{a..d}'
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_qemu qemu qemu-kvm qemu-system-i386 qemu-system-x86_64

# ex: filetype=sh
