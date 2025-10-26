# bash completion for smartctl(8)                          -*- shell-script -*-
# Updated for smartmontools 7.5 (released 2025-04-30)

_comp_cmd_smartctl__set_nospace_if_incomplete()
{
    local i
    for i in "${!COMPREPLY[@]}"; do
        if [[ ${COMPREPLY[i]} == *[,=] ]]; then
            compopt -o nospace
            break
        fi
    done
}
_comp_cmd_smartctl__device()
{
    case $cur in
        3ware,* | areca,* | cciss,* | megaraid,*)
            _comp_compgen -P "${cur%%,*}," -- -W '{0..31}'
            ;;
        aacraid,*,*,*,*) ;;
        aacraid,[0-7],[0-7],*)
            _comp_compgen -P "${cur%,*}," -- -W '{0..31}'
            ;;
        aacraid,*,*,*) ;;
        aacraid,[0-7],*)
            _comp_compgen -P "${cur%,*}," -- -W '{0..7},'
            compopt -o nospace
            ;;
        aacraid,*)
            _comp_compgen -P "aacraid," -- -W '{0..7},'
            compopt -o nospace
            ;;
        hpt,*/*/*/*) ;;
        hpt,[1-4]/[1-8]/*)
            _comp_compgen -P "${cur%/*}/" -- -W '{1..8}'
            ;;
        hpt,[1-4]/*)
            _comp_compgen -P "${cur%%/*}/" -- -W '{1..8}{,/}'
            compopt -o nospace
            ;;
        hpt,*)
            _comp_compgen -P "hpt," -- -W '{1..4}/'
            compopt -o nospace
            ;;
        jmb39x,* | jmb39x-q,* | jmb39x-q2,* | jms56x,*)
            _comp_compgen -P "${cur%%,*}," -- -W '{0..4}'
            ;;
        sssraid,*,*,*) ;;
        sssraid,[0-7],*)
            _comp_compgen -P "${cur%,*}," -- -W '{0..31}'
            ;;
        sssraid,*)
            _comp_compgen -P "sssraid," -- -W '{0..7},'
            compopt -o nospace
            ;;
        *)
            _comp_compgen -- -W 'auto test ata scsi nvme{,\,}
                sat{,\,auto}{,\,12} usb{jmicron,prolific,sunplus}
                snt{asmedia,jmicron,realtek}{,/sat} 3ware, aacraid, areca,
                cciss, hpt, megaraid, sssraid, jmb39x{,-q,-q2}, jms56x,'
            _comp_cmd_smartctl__set_nospace_if_incomplete
            ;;
    esac
}
_comp_cmd_smartctl__drivedb()
{
    local prefix=
    if [[ $cur == +* ]]; then
        prefix=+
        cur="${cur#+}"
    fi
    _comp_compgen_filedir h && [[ $prefix ]] &&
        _comp_compgen -Rv COMPREPLY -- -P "$prefix" -W '"${COMPREPLY[@]}"'
}
_comp_cmd_smartctl__vendorattribute()
{
    case $cur in
        [1-9N],* | [1-9][0-9],* | 1[0-9][0-9],* | 2[0-4][0-9],* | 25[0-5],*)
            # TODO: add 'raw16(raw16)', 'raw16(avg16)' and 'raw24(raw8)'.
            # Excluded for now because 'compopt -o fullquote' (Bash >= 5.3)
            # or similar bash_completion functionality would be required.
            _comp_compgen -P "${cur%%,*}," -- -W 'raw{8,16,48,56,64}
                hex{48,56,64} raw24/raw{24,32} msec24hour32
                {sec,min,halfmin}2hour temp{10x,minmax}'
            if ((${#COMPREPLY[@]} == 1)); then
                _comp_compgen -R -- -W '"$COMPREPLY"{,\,,:}'
            fi
            ;;
        [1-9] | [1-9][0-9] | 1[0-9][0-9] | 2[0-4][0-9] | 25[0-5])
            _comp_compgen -- -W '{1..255},'
            ;;
        *)
            _comp_compgen -- -W 'N, help'
            ;;
    esac
    compopt -o nospace
}
_comp_cmd_smartctl__set()
{
    _comp_compgen -- -W 'aam,{,off} apm,{,off} dsn,{on,off}
        lookahead,{on,off} rcache,{on,off} security-freeze standby,{,off,now}
        wcache,{on,off} wcache-sct,{ata,on,off}{,\,p}
        wcreorder,{on,off}{,\,p} '"$1"
    _comp_cmd_smartctl__set_nospace_if_incomplete
}

_comp_cmd_smartctl()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[qdTbrnoSlvFPBtfgs]*)'
    # shellcheck disable=SC2254
    case $prev in
        --quietmode | -${noargopts}q)
            _comp_compgen -- -W 'errorsonly silent noserial'
            return
            ;;
        --device | -${noargopts}d)
            _comp_cmd_smartctl__device
            return
            ;;
        --tolerance | -${noargopts}T)
            _comp_compgen -- -W 'normal conservative permissive verypermissive'
            return
            ;;
        --badsum | -${noargopts}b)
            _comp_compgen -- -W 'warn exit ignore'
            return
            ;;
        --report | -${noargopts}r)
            _comp_compgen -- -W '{,ata,scsi,nvme}ioctl{,\,2}'
            return
            ;;
        --nocheck | -${noargopts}n)
            _comp_compgen -- -W 'never sleep{,\,} standby{,\,} idle{,\,}'
            _comp_cmd_smartctl__set_nospace_if_incomplete
            return
            ;;
        --smart | --offlineauto | --saveauto | -${noargopts}[oS])
            _comp_compgen -- -W 'on off'
            return
            ;;
        --log | -${noargopts}l)
            _comp_compgen -- -W 'background defects{,\,} devstat{,\,}
                directory{,\,g,\,s} envrep error farm genstats gplog, nvmelog,
                sasphy{,\,reset} sataphy{,\,reset} scterc{,\,,\,p,\,reset}
                scttemp{,sts,int\,,hist} selective selftest smartlog, ssd
                tapealert tapedevstat xerror{,\,,\,error}
                xselftest{,\,,\,selftest} zdevstat'
            _comp_cmd_smartctl__set_nospace_if_incomplete
            return
            ;;
        --vendorattribute | -${noargopts}v)
            _comp_cmd_smartctl__vendorattribute
            return
            ;;
        --firmwarebug | -${noargopts}F)
            _comp_compgen -- -W 'none nologdir samsung{,2,3} swapid xerrorlba'
            return
            ;;
        --presets | -${noargopts}P)
            _comp_compgen -- -W 'use ignore show showall'
            return
            ;;
        --drivedb | -${noargopts}B)
            _comp_cmd_smartctl__drivedb
            return
            ;;
        --test | -${noargopts}t)
            _comp_compgen -- -W 'afterselect,{on,off} conveyance force long
                offline pending, scttempint, select,{,redo,next} short vendor,'
            _comp_cmd_smartctl__set_nospace_if_incomplete
            return
            ;;
        --format | -${noargopts}f)
            _comp_compgen -- -W 'brief hex{,\,id,\,val} old'
            return
            ;;
        --get | -${noargopts}g)
            _comp_compgen -- -W 'aam all apm dsn lookahead rcache security
                wcache{,-sct} wcreorder'
            return
            ;;
        --set)
            _comp_cmd_smartctl__set ''
            return
            ;;
        -${noargopts}s) # -s {on,off}: --smart {on,off}; -s OTHER: --set OTHER
            _comp_cmd_smartctl__set 'on off'
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        _comp_cmd_smartctl__set_nospace_if_incomplete
    else
        _comp_compgen -c "${cur:-/dev/}" filedir
    fi
} &&
    complete -F _comp_cmd_smartctl smartctl

# ex: filetype=sh
