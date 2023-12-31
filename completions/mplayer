# mplayer(1) completion                                    -*- shell-script -*-

_comp_cmd_mplayer__options()
{
    cur=${cur%\\}
    _comp_compgen_split -- "$("$1" -noconfig all "$2" help 2>/dev/null |
        command sed -e '/^Available/,/^$/!d' -e '/^Available/d' | _comp_awk '{print $1}' |
        command sed -e 's/:$//' -e 's/^'"${2#-}"'$//' -e 's/<.*//')"
}

_comp_cmd_mplayer()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    local cmd=${words[0]} i j k=0

    case $prev in
        -[av][cfo] | -[av]fm | -vop | -fstype | -demuxer | -o[av]c | -of | -profile | \
            -audio-demuxer | -sub-demuxer)
            _comp_cmd_mplayer__options "$cmd" "$prev"
            return
            ;;
        -show-profile)
            _comp_cmd_mplayer__options "$cmd" -profile
            return
            ;;
        -audiofile | -audio-file)
            _comp_compgen_filedir '@(mp3|mpg|og[ag]|w?(a)v|mid|flac|mka|ac3|ape)'
            return
            ;;
        -font | -subfont)
            if [[ $prev == -font ]]; then
                _comp_compgen_filedir '@(desc|ttf)'
            else
                _comp_compgen_filedir ttf
            fi
            _comp_compgen -a split -l -- "$(fc-list 2>/dev/null)"
            return
            ;;
        -sub | -sub-file)
            _comp_compgen_filedir '@(srt|sub|txt|utf|rar|mpsub|smi|js|ssa|ass)'
            return
            ;;
        -vobsub)
            if _comp_compgen_filedir '@(idx|ifo|sub)'; then
                for i in "${!COMPREPLY[@]}"; do
                    if [[ -f ${COMPREPLY[i]} && -r ${COMPREPLY[i]} ]]; then
                        COMPREPLY[i]=${COMPREPLY[i]%.*}
                    fi
                done
            fi
            return
            ;;
        -subcp | -msgcharset)
            local cp
            if _comp_split cp "$(iconv --list 2>/dev/null | command sed -e "s@//@@;" 2>/dev/null)"; then
                if [[ $cur == "${cur,,}" ]]; then
                    _comp_compgen -- -W '"${cp[@],,}"'
                else
                    _comp_compgen -- -W '"${cp[@]^^}"'
                fi
            fi
            return
            ;;
        -ifo)
            _comp_compgen_filedir ifo
            return
            ;;
        -cuefile)
            _comp_compgen_filedir '@(bin|cue)'
            return
            ;;
        -skin)
            # if you don't have installed mplayer in /usr you
            # may want to set the MPLAYER_SKINS_DIR global variable
            local -a dirs
            if [[ $MPLAYER_SKINS_DIR ]]; then
                _comp_split dirs "$MPLAYER_SKINS_DIR"
            else
                dirs=(/usr/share/mplayer/skins /usr/local/share/mplayer/skins)
            fi

            if ((${#dirs[@]})); then
                local -a subdirs
                for i in ~/.mplayer/skins "${dirs[@]}"; do
                    if [[ -d $i && -r $i ]]; then
                        _comp_compgen -v subdirs -c "$i/$cur" -- -d
                        for j in "${subdirs[@]}"; do
                            COMPREPLY[k++]=${j#"$i/"}
                        done
                    fi
                done
            fi
            return
            ;;
        -cdrom-device)
            _comp_compgen_cd_devices
            _comp_compgen -a dvd_devices
            return
            ;;
        -dvd-device)
            _comp_compgen_dvd_devices
            _comp_compgen -a filedir iso
            return
            ;;
        -bluray-device)
            _comp_compgen_filedir -d
            return
            ;;
        -mixer | -dvdauth | -fb | -zrdev)
            _comp_compgen -c "${cur:-/dev/}" filedir
            return
            ;;
        -edl | -edlout | -lircconf | -menu-cfg | -playlist | -csslib | -dumpfile | \
            -subfile | -aofile | -fbmodeconfig | -include | -o | -dvdkey | -passlogfile)
            _comp_compgen_filedir
            return
            ;;
        -autoq | -autosync | -loop | -menu-root | -speed | -sstep | -aid | -alang | \
            -bandwidth | -bluray-angle | -bluray-chapter | -cache | -chapter | -dvd-speed | \
            -dvdangle | -fps | -frames | -mc | -passwd | -user | -sb | -srate | -ss | -vcd | \
            -vi | -vid | -vivo | -ffactor | -sid | -slang | -spualign | -spuaa | -spugauss | \
            -vobsubid | -delay | -bpp | -brightness | -contrast | -dfbopts | -display | \
            -fbmode | -geometry | -guiwid | -hue | -icelayer | -screen[wh] | -wid | \
            -monitor-dotclock | -monitor-[hv]freq | -panscan | \
            -saturation | -xineramascreen | -zrcrop | -zrnorm | -zrquality | \
            -zr[xy]doff | -zr[vh]dec | -pp | -x | -y | -xy | -z | -stereo | \
            -audio-density | -audio-delay | -audio-preload | -endpos | -osdlevel | \
            -ffourcc | -sws | -skiplimit | -format | -ofps | -aadriver | \
            -aaosdcolor | -aasubcolor | -vobsubout | -vobsuboutid | -vobsuboutindex | \
            -sub-bg-alpha | -sub-bg-color | -subdelay | -subfps | -subpos | \
            -subalign | -subwidth | -subfont-blur | -subfont-outline | \
            -subfont-autoscale | -subfont-encoding | -subfont-osd-scale | \
            -subfont-text-scale)
            return
            ;;
        -channels)
            _comp_compgen -- -W '2 4 6 8'
            return
            ;;
        -aspect | -monitoraspect)
            _comp_compgen -- -W '1:1 3:2 4:3 5:4 14:9 14:10 16:9 16:10 2.35:1'
            _comp_ltrim_colon_completions "$cur"
            return
            ;;
        -lavdopts)
            _comp_compgen -- -W 'bitexact bug= debug= ec= er= fast gray idct=
                lowres= sb= st= skiploopfilter= skipidct= skipframe= threads=
                vismv= vstats'
            return
            ;;
        -lavcopts)
            _comp_compgen -- -W 'vcodec= vqmin= vqscale= vqmax= mbqmin= mbqmax=
                vqdiff= vmax_b_frames= vme= vhq v4mv keyint= vb_strategy=
                vpass= aspect= vbitrate= vratetol= vrc_maxrate= vrc_minrate=
                vrc_buf_size= vb_qfactor= vi_qfactor= vb_qoffset= vi_qoffset=
                vqblur= vqcomp= vrc_eq= vrc_override= vrc_init_cplx= vqsquish=
                vlelim= vcelim= vstrict= vdpart vpsize= gray vfdct= idct=
                lumi_mask= dark_mask= tcplx_mask= scplx_mask= naq ildct format=
                pred qpel precmp= cmp= subcmp= predia= dia= trell last_pred=
                preme= subq= psnr mpeg_quant aic umv'
            return
            ;;
        -ssf)
            _comp_compgen -- -W 'lgb= cgb= ls= cs= chs= cvs='
            return
            ;;
        -jpeg)
            _comp_compgen -- -W 'noprogressive progressive nobaseline baseline
                optimize= smooth= quality= outdir='
            return
            ;;
        -xvidopts)
            _comp_compgen -- -W 'dr2 nodr2'
            return
            ;;
        -xvidencopts)
            _comp_compgen -- -W 'pass= bitrate= fixed_quant= me_quality= 4mv
                rc_reaction_delay_factor= rc_averaging_period= rc_buffer=
                quant_range= min_key_interval= max_key_interval= mpeg_quant
                mod_quant lumi_mask hintedme hintfile debug keyframe_boost=
                kfthreshold= kfreduction='
            return
            ;;
        -divx4opts)
            _comp_compgen -- -W 'br= key= deinterlace q= min_quant= max_quant=
                rc_period= rc_reaction_period= crispness= rc_reaction_ratio=
                pass= vbrpass= help'
            return
            ;;
        -info)
            _comp_compgen -- -W 'name= artist= genre= subject= copyright=
                srcform= comment= help'
            return
            ;;
        -lameopts)
            _comp_compgen -- -W 'vbr= abr cbr br= q= aq= ratio= vol= mode=
                padding= fast preset= help'
            return
            ;;
        -rawaudio)
            _comp_compgen -- -W 'on channels= rate= samplesize= format='
            return
            ;;
        -rawvideo)
            _comp_compgen -- -W 'on fps= sqcif qcif cif 4cif pal ntsc w= h=
                y420 yv12 yuy2 y8 format= size='
            return
            ;;
        -aop)
            _comp_compgen -- -W 'list= delay= format= fout= volume= mul=
                softclip'
            return
            ;;
        -dxr2)
            _comp_compgen -- -W 'ar-mode= iec958-encoded iec958-decoded mute
                ucode= 75ire bw color interlaced macrovision= norm=
                square-pixel ccir601-pixel cr-left= cr-right= cr-top= cr-bot=
                ck-rmin= ck-gmin= ck-bmin= ck-rmax= ck-gmax= ck-bmax= ck-r=
                ck-g= ck-b= ignore-cache= ol-osd= olh-cor= olw-cor= olx-cor=
                oly-cor= overlay overlay-ratio= update-cache'
            return
            ;;
        -tv)
            _comp_compgen -- -W 'on noaudio driver= device= input= freq=
                outfmt= width= height= buffersize= norm= channel= chanlist=
                audiorate= forceaudio alsa amode= forcechan= adevice= audioid=
                volume= bass= treble= balance= fps= channels= immediatemode='
            return
            ;;
        -mf)
            _comp_compgen -- -W 'on w= h= fps= type='
            return
            ;;
        -cdda)
            _comp_compgen -- -W 'speed= paranoia= generic-dev= sector-size=
                overlap= toc-bias toc-offset= skip noskip'
            return
            ;;
        -input)
            _comp_compgen -- -W 'conf= ar-delay ar-rate keylist cmdlist js-dev
                file'
            return
            ;;
        -af-adv)
            _comp_compgen -- -W 'force= list='
            return
            ;;
        -noconfig)
            _comp_compgen -- -W 'all gui system user'
            return
            ;;
        -*)
            # Assume arg is required for everything else except options
            # for which -list-options says Type is Flag or Print.
            $cmd -noconfig all -list-options 2>/dev/null |
                while read -r i j k; do
                    if [[ $i == "${prev#-}" ]]; then
                        [[ ${j,,} != @(flag|print) ]] && return 1
                        break
                    fi
                done || return
            ;;
    esac

    case $cur in
        -*)
            _comp_compgen_split -- "$("$cmd" -noconfig all -list-options 2>/dev/null |
                command sed -ne "1,/^[[:space:]]*Name/d" \
                    -e "s/^[[:space:]]*/-/" -e "s/[[:space:]:].*//" \
                    -e "/^-\(Total\|.*\*\)\{0,1\}$/!p")"
            ;;
        *)
            _comp_compgen_filedir '@(m?(j)p?(e)g|M?(J)P?(E)G|wm[av]|WM[AV]|avi|AVI|asf|ASF|vob|VOB|bin|BIN|dat|DAT|vcd|VCD|ps|PS|pes|PES|fl[iv]|FL[IV]|fxm|FXM|viv|VIV|rm?(j)|RM?(J)|ra?(m)|RA?(M)|yuv|YUV|mov|MOV|qt|QT|mp[234]|MP[234]|m?(p)4[av]|M?(P)4[AV]|og[gmavx]|OG[GMAVX]|w?(a)v|W?(A)V|dump|DUMP|mk[av]|MK[AV]|aac|AAC|m2v|M2V|dv|DV|rmvb|RMVB|mid|MID|t[ps]|T[PS]|3g[p2]|3gpp?(2)|mpc|MPC|flac|FLAC|vro|VRO|divx|DIVX|aif?(f)|AIF?(F)|m2t?(s)|M2T?(S)|mts|MTS|vdr|VDR|xvid|XVID|ape|APE|gif|GIF|nut|NUT|bik|BIK|web[am]|WEB[AM]|amr|AMR|awb|AWB|iso|ISO|opus|OPUS|m[eo]d|M[EO]D|xm|XM|it|IT|s[t3]m|S[T3]M|mtm|MTM|w64|W64)?(.@(crdownload|part))'
            ;;
    esac

} &&
    complete -F _comp_cmd_mplayer mplayer mplayer2 mencoder gmplayer kplayer

# ex: filetype=sh
