# bash completion for lvm                                  -*- shell-script -*-

_comp_cmd_lvm__filedir()
{
    _comp_compgen -c "${cur:-/dev/}" filedir
}

_comp_cmd_lvm__volumegroups()
{
    _comp_compgen_split -- "$(vgscan 2>/dev/null |
        command sed -n -e 's|.*Found.*"\(.*\)".*$|\1|p')"
}

_comp_cmd_lvm__physicalvolumes_all()
{
    _comp_compgen_split -- "$(pvscan 2>/dev/null |
        command sed -n -e 's|^.*PV \([^ ]*\) .*|\1|p')"
}

_comp_cmd_lvm__physicalvolumes()
{
    _comp_compgen_split -- "$(pvscan 2>/dev/null |
        command sed -n -e 's|^.*PV \(.*\) VG.*$|\1|p')"
}

_comp_cmd_lvm__logicalvolumes()
{
    _comp_compgen_split -- "$(lvscan 2>/dev/null |
        command sed -n -e "s|^.*'\(.*\)'.*$|\1|p")"
    if [[ $cur == /dev/mapper/* ]]; then
        _comp_compgen -a filedir
        local i
        for i in "${!COMPREPLY[@]}"; do
            [[ ${COMPREPLY[i]} == */control ]] && unset -v 'COMPREPLY[i]'
        done
    fi
}

_comp_cmd_lvm__units()
{
    _comp_compgen -- -W 'h s b k m g t H K M G T'
}

_comp_cmd_lvm__sizes()
{
    _comp_compgen -- -W 'k K m M g G t T'
}

# @param $1 glob matching args known to take an argument
_comp_cmd_lvm__count_args()
{
    REPLY=0
    local offset=1
    if [[ ${words[0]} == lvm ]]; then
        offset=2
    fi
    local i prev=${words[offset - 1]}
    for ((i = offset; i < cword; i++)); do
        # shellcheck disable=SC2053
        if [[ ${words[i]} != -* && $prev != $1 ]]; then
            ((REPLY++))
        fi
        prev=${words[i]}
    done
}

_comp_cmd_lvmdiskscan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    fi
} &&
    complete -F _comp_cmd_lvmdiskscan lvmdiskscan

_comp_cmd_pvscan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    fi
} &&
    complete -F _comp_cmd_pvscan pvscan

_comp_cmd_pvs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[oO]*)'
    # shellcheck disable=SC2254
    case $prev in
        --options | --sort | -${noargopts}[oO])
            _comp_compgen -- -W 'pv_fmt pv_uuid pv_size pv_free pv_used pv_name
                pv_attr pv_pe_count pv_pe_alloc_count'
            return
            ;;
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__physicalvolumes_all
    fi
} &&
    complete -F _comp_cmd_pvs pvs

_comp_cmd_pvdisplay()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__physicalvolumes_all
    fi
} &&
    complete -F _comp_cmd_pvdisplay pvdisplay

_comp_cmd_pvchange()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[Ax]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | --allocatable | -${noargopts}[Ax])
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__physicalvolumes_all
    fi
} &&
    complete -F _comp_cmd_pvchange pvchange

_comp_cmd_pvcreate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[M]*)'
    # shellcheck disable=SC2254
    case $prev in
        --restorefile)
            _comp_compgen_filedir
            return
            ;;
        --metadatatype | -${noargopts}M)
            _comp_compgen -- -W '1 2'
            return
            ;;
        --metadatacopies)
            _comp_compgen -- -W '0 1 2'
            return
            ;;
        --metadatasize | --setphysicalvolumesize)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__filedir
    fi
} &&
    complete -F _comp_cmd_pvcreate pvcreate

_comp_cmd_pvmove()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[An]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --name | -${noargopts}n)
            _comp_cmd_lvm__logicalvolumes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__physicalvolumes
    fi
} &&
    complete -F _comp_cmd_pvmove pvmove

_comp_cmd_pvremove()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__physicalvolumes_all
    fi
} &&
    complete -F _comp_cmd_pvremove pvremove

_comp_cmd_vgscan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    fi
} &&
    complete -F _comp_cmd_vgscan vgscan

_comp_cmd_vgs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[oO]*)'
    # shellcheck disable=SC2254
    case $prev in
        --options | --sort | -${noargopts}[oO])
            _comp_compgen -- -W 'vg_fmt vg_uuid vg_name vg_attr vg_size vg_free
                vg_sysid vg_extent_size vg_extent_count vg_free_count max_lv
                max_pv pv_count lv_count snap_count vg_seqno'
            return
            ;;
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgs vgs

_comp_cmd_vgdisplay()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgdisplay vgdisplay

_comp_cmd_vgchange()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[aAx]*)'
    # shellcheck disable=SC2254
    case $prev in
        --available | --autobackup | --resizeable | -${noargopts}[aAx])
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgchange vgchange

_comp_cmd_vgcreate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AMs]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --metadatatype | -${noargopts}M)
            _comp_compgen -- -W '1 2'
            return
            ;;
        --physicalextentsize | -${noargopts}s)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup|-M|--metadatatype|-s|--physicalextentsize)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__volumegroups
        else
            _comp_cmd_lvm__physicalvolumes_all
        fi
    fi
} &&
    complete -F _comp_cmd_vgcreate vgcreate

_comp_cmd_vgremove()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgremove vgremove

_comp_cmd_vgrename()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[A]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgrename vgrename

_comp_cmd_vgreduce()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[A]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help

    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__volumegroups
        else
            _comp_cmd_lvm__physicalvolumes
        fi
    fi
} &&
    complete -F _comp_cmd_vgreduce vgreduce

_comp_cmd_vgextend()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AL]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --size | -${noargopts}L)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup|-L|--size)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__volumegroups
        else
            _comp_cmd_lvm__physicalvolumes_all
        fi
    fi
} &&
    complete -F _comp_cmd_vgextend vgextend

_comp_cmd_vgport()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgport vgimport vgexport

_comp_cmd_vgck()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgck vgck

_comp_cmd_vgconvert()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[M]*)'
    # shellcheck disable=SC2254
    case $prev in
        --metadatatype | -${noargopts}M)
            _comp_compgen -- -W '1 2'
            return
            ;;
        --metadatacopies)
            _comp_compgen -- -W '0 1 2'
            return
            ;;
        --metadatasize)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgconvert vgconvert

_comp_cmd_vgcfgbackup()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[f]*)'
    # shellcheck disable=SC2254
    case $prev in
        --file | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgcfgbackup vgcfgbackup

_comp_cmd_vgcfgrestore()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[fMn]*)'
    # shellcheck disable=SC2254
    case $prev in
        --file | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
        --metadatatype | -${noargopts}M)
            _comp_compgen -- -W '1 2'
            return
            ;;
        --name | -${noargopts}n)
            _comp_cmd_lvm__volumegroups
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgcfgrestore vgcfgrestore

_comp_cmd_vgmerge()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[A]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgmerge vgmerge

_comp_cmd_vgsplit()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AM]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --metadatatype | -${noargopts}M)
            _comp_compgen -- -W '1 2'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup|-M|--metadatatype)'
        if ((REPLY < 2)); then
            _comp_cmd_lvm__volumegroups
        else
            _comp_cmd_lvm__physicalvolumes
        fi
    fi
} &&
    complete -F _comp_cmd_vgsplit vgsplit

_comp_cmd_vgmknodes()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__volumegroups
    fi
} &&
    complete -F _comp_cmd_vgmknodes vgmknodes

_comp_cmd_lvscan()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    fi
} &&
    complete -F _comp_cmd_lvscan lvscan

_comp_cmd_lvs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[oO]*)'
    # shellcheck disable=SC2254
    case $prev in
        --options | --sort | -${noargopts}[oO])
            _comp_compgen -- -W 'lv_uuid lv_name lv_attr lv_minor lv_size
                seg_count origin snap_percent segtype stripes stripesize
                chunksize seg_start seg_size'
            return
            ;;
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvs lvs

_comp_cmd_lvdisplay()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --units)
            _comp_cmd_lvm__units
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvdisplay lvdisplay

_comp_cmd_lvchange()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[aACMp]*)'
    # shellcheck disable=SC2254
    case $prev in
        --available | --autobackup | --contiguous | --persistent | -${noargopts}[aACM])
            _comp_compgen -- -W 'y n'
            return
            ;;
        --permission | -${noargopts}p)
            _comp_compgen -- -W 'r rw'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvchange lvchange

_comp_cmd_lvcreate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[ACMZLpn]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | --contiguous | --persistent | --zero | -${noargopts}[ACMZ])
            _comp_compgen -- -W 'y n'
            return
            ;;
        --size | -${noargopts}L)
            _comp_cmd_lvm__sizes
            return
            ;;
        --permission | -${noargopts}p)
            _comp_compgen -- -W 'r rw'
            return
            ;;
        --name | -${noargopts}n)
            _comp_cmd_lvm__logicalvolumes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|-C|-M|-Z|--autobackup|--contiguous|--persistent|--zero|-L|--size|-p|--permission|-n|--name)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__volumegroups
        else
            _comp_cmd_lvm__physicalvolumes
        fi
    fi
} &&
    complete -F _comp_cmd_lvcreate lvcreate

_comp_cmd_lvremove()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[A]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvremove lvremove

_comp_cmd_lvrename()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[A]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvrename lvrename

_comp_cmd_lvreduce()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AL]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --size | -${noargopts}L)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        _comp_cmd_lvm__logicalvolumes
    fi
} &&
    complete -F _comp_cmd_lvreduce lvreduce

_comp_cmd_lvresize()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AL]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --size | -${noargopts}L)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup|-L|--size)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__logicalvolumes
        else
            _comp_cmd_lvm__physicalvolumes
        fi
    fi
} &&
    complete -F _comp_cmd_lvresize lvresize

_comp_cmd_lvextend()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local noargopts='!(-*|*[AL]*)'
    # shellcheck disable=SC2254
    case $prev in
        --autobackup | -${noargopts}A)
            _comp_compgen -- -W 'y n'
            return
            ;;
        --size | -${noargopts}L)
            _comp_cmd_lvm__sizes
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- --help
    else
        local REPLY
        _comp_cmd_lvm__count_args '@(-A|--autobackup|-L|--size)'
        if ((REPLY == 0)); then
            _comp_cmd_lvm__logicalvolumes
        else
            _comp_cmd_lvm__physicalvolumes
        fi
    fi
} &&
    complete -F _comp_cmd_lvextend lvextend

_comp_cmd_lvm()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'dumpconfig help lvchange lvcreate lvdisplay
            lvextend lvmchange lvmdiskscan lvmsadc lvmsar lvreduce lvremove
            lvrename lvresize lvs lvscan pvchange pvcreate pvdata pvdisplay
            pvmove pvremove pvresize pvs pvscan vgcfgbackup vgcfgrestore
            vgchange vgck vgconvert vgcreate vgdisplay vgexport vgextend
            vgimport vgmerge vgmknodes vgreduce vgremove vgrename vgs vgscan
            vgsplit version'
    else
        case "${words[1]}" in
            pvchange | pvcreate | pvdisplay | pvmove | pvremove | pvresize | pvs | pvscan | \
                vgcfgbackup | vgcfgrestore | vgchange | vgck | vgconvert | vgcreate | \
                vgdisplay | vgexport | vgextend | vgimport | vgmerge | vgmknodes | vgreduce | \
                vgremove | vgrename | vgs | vgscan | vgsplit | lvchange | lvcreate | lvdisplay | \
                lvextend | lvreduce | lvremove | lvrename | lvresize | lvscan)
                _comp_command_offset 1
                ;;
        esac
    fi
} &&
    complete -F _comp_cmd_lvm lvm

# ex: filetype=sh
