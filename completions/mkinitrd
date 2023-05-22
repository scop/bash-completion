# bash completion for mkinitrd                             -*- shell-script -*-

_comp_cmd_mkinitrd()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    case $prev in
        --preload | --with | --builtin)
            _comp_compgen_kernel_modules
            return
            ;;
        --fstab | --dsdt)
            _comp_compgen_filedir
            return
            ;;
        --net-dev)
            _comp_compgen_available_interfaces
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--version --help -v -f --preload
            --force-scsi-probe --omit-scsi-modules --omit-ide-modules
            --image-version --force-raid-probe --omit-raid-modules --with=
            --force-lvm-probe --omit-lvm-modules --builtin --omit-dmraid
            --net-dev --fstab --nocompress --dsdt --bootchart'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        local REPLY
        _comp_count_args

        case $REPLY in
            1)
                _comp_compgen_filedir
                ;;
            2)
                _comp_compgen_kernel_versions
                ;;
        esac
    fi

} &&
    complete -F _comp_cmd_mkinitrd mkinitrd

# ex: filetype=sh
