# adb completion                                           -*- shell-script -*-

# Use of this file is deprecated.  Upstream completion is available in
# the Android SDK, use that instead.

_comp_cmd_adb__command_usage()
{
    _comp_compgen_help - <<<"$("$1" help 2>&1 |
        command sed -e "/^ *\(adb \)\{0,1\} *$2 /!d;s/[]|[]/\n/g")"
}

_comp_cmd_adb()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -s | -p | --algo | --key | --iv)
            return
            ;;
        -f)
            _comp_compgen_filedir
            return
            ;;
    esac

    local cmd has_cmd="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} != -* && ${words[i - 1]} != -[sp] ]]; then
            cmd="${words[i]}"
            has_cmd=set
            break
        fi
    done

    if [[ ! $has_cmd ]]; then
        local tmp=()
        if [[ ! $cur || $cur == -* ]]; then
            _comp_compgen -av tmp help -- help
        fi
        if [[ ! $cur || $cur != -* ]]; then
            _comp_split -a tmp "$("$1" help 2>&1 | _comp_awk '$1 == "adb" { print $2 }')"
            tmp+=(devices connect disconnect sideload)
        fi
        ((${#tmp[@]})) &&
            _comp_compgen -- -W '"${tmp[@]}"'
        return
    fi

    # TODO: more and better command completions

    _comp_cmd_adb__command_usage "$1" "$cmd"

    case $cmd in
        push | restore | sideload)
            _comp_compgen -a filedir
            ;;
        forward)
            _comp_compgen_help - <<<"$("$1" help 2>&1 |
                command sed -ne "s/^ *adb  *forward  *-/-/p")"
            ;;
        reboot)
            _comp_compgen -- -W 'bootloader recovery'
            ;;
    esac
} &&
    complete -F _comp_cmd_adb adb

# ex: filetype=sh
