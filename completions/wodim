# bash completion for cdrecord/wodim                       -*- shell-script -*-

_comp_cmd_wodim()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    local generic_options track_options track_mode

    # foo=bar style option
    if [[ $cur == *=* ]]; then
        prev=${cur%%=*}
        cur=${cur#*=}
        case $prev in
            textfile | cuefile | msifile)
                _comp_compgen_filedir
                ;;
            blank)
                _comp_compgen -- -W 'help all fast track unreserve trtail
                    unclose session'
                ;;
            driveropts)
                if [[ $cur == *=* ]]; then
                    prev=${cur%%=*}
                    cur=${cur#*=}
                    case $prev in
                        varirec)
                            _comp_compgen -- -W "-2 -1 0 1 2"
                            ;;
                        gigarec)
                            _comp_compgen -- -W "0.6 0.7 0.8 1.0 1.2 1.3 1.4"
                            ;;
                        tattoofile)
                            _comp_compgen_filedir
                            ;;
                    esac
                else
                    _comp_compgen -- -W 'burnfree noburnfree varirec= gigarec=
                        audiomaster forcespeed noforcespeed speedread
                        nospeedread singlesession nosinglesession hidecdr
                        nohidecdr tattooinfo tattoofile='
                    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
                fi
                ;;
            driver)
                _comp_compgen_split -- "$("$1" driver=help 2>&1 |
                    _comp_awk 'NR > 1 { print $1 }') help"
                ;;
            minbuf)
                _comp_compgen -- -W '{25..95}'
                ;;
        esac
        return
    fi

    generic_options=(-version -v -V -d -silent -force -immed -dummy -clone
        -dao -sao -tao -raw -raw96r -raw96p -raw16 -multi -msinfo -toc -atip
        -fix -nofix -waiti -load -lock -eject -format -setdropts -checkdrive
        -prcap -inq -scanbus --devices -reset -abort -overburn -ignsize
        -useinfo -packet -noclose -text "debug=" "kdebug=" "minbuf="
        "msifile=" "speed=" "blank=" "fs=" "ts=" "dev=" "gracetime="
        "timeout=" "driver=" "driveropts=" "defpregap=" "pktsize=" "mcn="
        "textfile=" "cuefile=")
    track_options=(-audio -swab -data -mode2 -xa -xa1 -xa2 -xamix -cdi
        -isosize -pad -nopad -shorttrack -noshorttrack -preemp -nopreemp
        -copy -nocopy -scms "isrc=" "index=" "padsize=" "pregap=" "tsize=")
    # look if previous was either a file or a track option
    track_mode=""
    if ((cword > 1)); then
        if [[ -f $prev ]]; then
            track_mode=set
        else
            local opt
            for opt in "${track_options[@]}"; do
                if [[ $opt == "$prev" ]]; then
                    track_mode=set
                    break
                fi
            done
        fi
    fi

    # files are always eligible completion
    _comp_compgen_filedir
    # track options are always available
    _comp_compgen -a -- -W '"${track_options[@]}"'
    # general options are no more available after file or track option
    if [[ ! $track_mode ]]; then
        _comp_compgen -a -- -W '"${generic_options[@]}"'
    fi
    [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
} &&
    complete -F _comp_cmd_wodim wodim cdrecord

# ex: filetype=sh
