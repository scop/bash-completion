# bash completion for cryptsetup                           -*- shell-script -*-

_comp_cmd_cryptsetup__name()
{
    _comp_compgen_split -X control -- "$(command ls /dev/mapper)"
}

_comp_cmd_cryptsetup__device()
{
    _comp_compgen -c "${cur:-/dev/}" filedir
}

_comp_cmd_cryptsetup__action()
{
    local REPLY IFS=$' \t\n'
    _comp_dequote "${1-}" || return 1
    local cmd=${REPLY:-cryptsetup}
    local -a actions
    _comp_split -l actions "$(
        {
            LC_ALL=C "$cmd" --help 2>&1 |
                command sed -n '
                    /^<action> is one of:$/,/^[^[:space:]]/s/^[[:space:]]\{1,\}\([^[:space:]]\{1,\}\).*/\1/p
                    /^You can also use old <action> syntax aliases:$/,/^[^[:space:]]/{/^[[:space:]]\{1,\}/!d;s///;s/[:(),[:space:]]\{1,\}/\n/gp;}
                '
            LC_ALL=C man cryptsetup 2>&1 |
                _comp_awk '/^[[:space:]]+[[:alnum:]_]+([[:space:]]+(-[^[:space:].]+|<[^<>]+>|\[[^][]+\]|\(.*\)|or))+$/ && $1 != "cryptsetup" {print $1}'
        } | sort -u
    )"

    if ((${#actions[@]} == 0)); then
        # The fallback action list is extracted from the following sources:
        # - https://gitlab.com/cryptsetup/cryptsetup/-/blob/main/src/cryptsetup.c#L3154-3208 (search for "Handle aliases")
        # - https://gitlab.com/cryptsetup/cryptsetup/-/blob/main/src/cryptsetup.c#L2831-2867 (search for "struct action_type")
        # - https://gitlab.com/cryptsetup/cryptsetup/-/blob/main/src/cryptsetup_args.h#L28-53 (see the macros "*_ACTION")
        # - The outputs of "cryptsetup --help" and "man cryptsetup" for
        #   cryptsetup-2.7.5: "fvault2Close", "fvault2Dump", "fvault2Open", and
        #   "tcryptOpen_" are added.
        actions=(benchmark bitlkClose bitlkDump bitlkOpen close config convert
            create erase fvault2Close fvault2Dump fvault2Open isLuks
            loopaesClose loopaesOpen luksAddKey luksChangeKey luksClose
            luksConfig luksConvertKey luksDump luksErase luksFormat
            luksHeaderBackup luksHeaderRestore luksKillSlot luksOpen
            luksRemoveKey luksResume luksSuspend luksUUID open plainClose
            plainOpen reencrypt refresh remove repair resize status tcryptClose
            tcryptDump tcryptOpen tcryptOpen_ token)

        # We attempt to filter the supported actions by the strings in the binary.
        local path
        if path=$(type -P -- "$cmd" 2>/dev/null || type -P -- cryptsetup 2>/dev/null); then
            local filtering_pattern
            printf -v filtering_pattern '%s\n' "${actions[@]}"
            filtering_pattern=${filtering_pattern%$'\n'}

            local filtered_actions
            filtered_actions=$(strings "$path" 2>/dev/null | command grep -Fx "$filtering_pattern" | sort -u) &&
                [[ $filtered_actions ]] &&
                _comp_split -l actions "$filtered_actions"
        fi
    fi

    _comp_compgen -- -W '"${actions[@]}"'
}

_comp_cmd_cryptsetup()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[cslSbopitTdM]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --cipher | --hash | --*-size | --key-slot | --size | --offset | \
            --skip | --iter-time | --timeout | --tries | -${noargopts}[chslSbopitT])
            return
            ;;
        --key-file | --master-key-file | --header | --header-backup-file | -${noargopts}d)
            _comp_compgen_filedir
            return
            ;;
        --type | -${noargopts}M)
            _comp_compgen -- -W "luks plain loopaes tcrypt"
            return
            ;;
    esac

    [[ $was_split ]] && return

    local REPLY
    if _comp_get_first_arg; then
        local arg=$REPLY
        _comp_count_args -a "-${noargopts}[chslSbopitTdM]"
        local args=$REPLY
        case $arg in
            open | create | luksOpen | loopaesOpen | tcryptOpen)
                case $args in
                    2)
                        _comp_cmd_cryptsetup__device
                        ;;
                    3)
                        _comp_cmd_cryptsetup__name
                        ;;
                esac
                ;;
            close | remove | luksClose | loopaesClose | tcryptClose | status | resize | \
                luksSuspend | luksResume)
                case $args in
                    2)
                        _comp_cmd_cryptsetup__name
                        ;;
                esac
                ;;
            luksFormat | luksAddKey | luksRemoveKey | luksChangeKey)
                case $args in
                    2)
                        _comp_cmd_cryptsetup__device
                        ;;
                    3)
                        _comp_compgen_filedir
                        ;;
                esac
                ;;
            luksKillSlot | luksDelKey | luksUUID | isLuks | luksDump)
                case $args in
                    2)
                        _comp_cmd_cryptsetup__device
                        ;;
                esac
                ;;
            luksHeaderBackup | luksHeaderRestore)
                case $args in
                    2)
                        _comp_cmd_cryptsetup__device
                        ;;
                    3)
                        COMPREPLY=('--header-backup-file')
                        ;;
                esac
                ;;
        esac
    else
        if [[ $cur == -* ]]; then
            _comp_compgen_help
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        else
            _comp_cmd_cryptsetup__action "$1"
        fi
    fi

} &&
    complete -F _comp_cmd_cryptsetup cryptsetup

# ex: filetype=sh
