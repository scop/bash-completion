# bash completion for xrandr                               -*- shell-script -*-

_comp_cmd_xrandr__compgen_outputs()
{
    _comp_compgen_split -- "$("$1" -q 2>/dev/null | _comp_awk '/connected/ {print $1}')"
}

_comp_cmd_xrandr__compgen_monitors()
{
    _comp_compgen_split -- "$(
        "$1" --listmonitors 2>/dev/null |
            command sed -ne 's/.* [0-9]*: [+\*]*\([^ ]*\).*/\1/p'
    )"
}

_comp_cmd_xrandr__compgen_providers()
{
    _comp_compgen_split -- "$("$1" --listproviders 2>/dev/null |
        command sed -ne "s/.*cap:.*$2.* name:\([^ ]*\).*/\1/p")"
}

_comp_cmd_xrandr__compgen_modes()
{
    _comp_compgen_split -- "$(
        "$1" -q 2>/dev/null | command sed \
            -e "1,/^$2 / d" \
            -e '/connected/,$ d' \
            -e '/^[[:space:]]*h: / d' \
            -e '/^[[:space:]]*v: / d' \
            -e 's/\([^[:space:]]\)[[:space:]].*/\1/'
    )"
}

_comp_cmd_xrandr__compgen_all_modes()
{
    _comp_compgen_split -- "$(
        "$1" -q 2>/dev/null | command sed \
            -e '/^[^[:space:]].*/ d' \
            -e '/^[[:space:]]*h: / d' \
            -e '/^[[:space:]]*v: / d' \
            -e 's/[[:space:]]*\([^[:space:]]*\)[[:space:]].*/\1/'
    )"
}

_comp_cmd_xrandr()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local i output has_output=""
    for ((i = cword - 1; i > 0; i--)); do
        if [[ ${words[i]} == --output ]]; then
            output=${words[i + 1]}
            has_output=set
            break
        fi
    done

    case "$prev" in
        -display | -d | -s | --size | -r | --rate | --refresh | --screen | \
            --fb | --fbmm | --pos | --set | --scale | --transform | --crtc | \
            --panning | --gamma | --newmode | --rmmode | --setmonitor)
            return
            ;;
        --output | --addmode | --delmode | --dpi)
            _comp_cmd_xrandr__compgen_outputs "$1"
            return
            ;;
        --left-of | --right-of | --above | --below | --same-as)
            if [[ $has_output ]]; then
                _comp_cmd_xrandr__compgen_outputs "$1"
            fi
            return
            ;;
        --mode)
            if [[ $has_output ]]; then
                _comp_cmd_xrandr__compgen_modes "$1" "$output"
            fi
            return
            ;;
        -o | --orientation)
            _comp_compgen -- -W 'normal inverted left right 0 1 2 3'
            return
            ;;
        --reflect)
            if [[ $has_output ]]; then
                _comp_compgen -- -W 'normal x y xy'
            fi
            return
            ;;
        --rotate)
            if [[ $has_output ]]; then
                _comp_compgen -- -W 'normal inverted left right'
            fi
            return
            ;;
        --filter)
            if [[ $has_output ]]; then
                _comp_compgen -- -W 'bilinear nearest'
            fi
            return
            ;;
        --setprovideroutputsource)
            _comp_cmd_xrandr__compgen_providers "$1" "Sink Output"
            return
            ;;
        --setprovideroffloadsink)
            _comp_cmd_xrandr__compgen_providers "$1" "Source Offload"
            return
            ;;
        --delmonitor)
            _comp_cmd_xrandr__compgen_monitors "$1"
            return
            ;;
    esac

    # second arguments
    if ((cword >= 2)); then
        case "${words[cword - 2]}" in
            --set)
                return
                ;;
            --addmode)
                _comp_cmd_xrandr__compgen_all_modes "$1"
                return
                ;;
            --delmode)
                _comp_cmd_xrandr__compgen_modes "$1" "${words[cword - 1]}"
                return
                ;;
            --setmonitor)
                _comp_compgen -- -W 'auto'
                return
                ;;
            --setprovideroutputsource)
                _comp_cmd_xrandr__compgen_providers "$1" "Source Output"
                _comp_compgen -a -- -W "0x0"
                return
                ;;
            --setprovideroffloadsink)
                _comp_cmd_xrandr__compgen_providers "$1" "Sink Offload"
                _comp_compgen -a -- -W "0x0"
                return
                ;;
        esac
    fi

    # third arguments
    if ((cword >= 3)); then
        case "${words[cword - 3]}" in
            --setmonitor)
                _comp_compgen -c "${cur##*,}" -i xrandr outputs "$1"
                _comp_compgen -ac "${cur##*,}" -- -W "none"
                _comp_delimited , -W '"${COMPREPLY[@]}"'
                return
                ;;
        esac
    fi

    local options
    if [[ $has_output ]]; then
        _comp_compgen -v options help - <<<"$(
            "$1" --help 2>/dev/null |
                command sed -e 's/ or /\n  /g' -e 's/<[^>]*>]//g'
        )"
    else
        # if no output is specified, remove per-output options
        _comp_compgen -v options help - <<<"$(
            "$1" --help 2>/dev/null |
                command sed -e '/^  -/!d' -e 's/ or /\n  /g' -e 's/<[^>]*>]//g'
        )"
    fi

    _comp_compgen -- -W '"${options[@]}"'
} &&
    complete -F _comp_cmd_xrandr xrandr

# ex: filetype=sh
