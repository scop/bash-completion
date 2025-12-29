# bash completion for fbi(1)                               -*- shell-script -*-

_comp_cmd_fbi()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
        -l | --list)
            _comp_compgen_filedir
            return
            ;;
        -r | --resolution)
            _comp_compgen -aR -- -W '{1..5}'
            return
            ;;
        -f | --font)
            _comp_compgen_split -l -- "$(fc-list 2>/dev/null)"
            return
            ;;
        -m | --mode)
            _comp_compgen_split -- "$(command sed \
                -n '/^mode/{s/^mode \{1,\}"\([^"]\{1,\}\)"/\1/g;p}' \
                /etc/fb.modes 2>/dev/null)"
            return
            ;;
        -d | --device)
            _comp_compgen -c "${cur:-/dev/}" -- -f -d
            return
            ;;
        --cachemem | --blend | -T | --vt | -s | --scroll | -t | --timeout | -g | --gamma)
            # argument required but no completions available
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--help --version --store --list --text --autozoom
            --{,no}autoup --{,no}autodown --{,no}fitwidth --{,no}verbose
            --{,no}random --{,no}comments --{,no}edit --{,no}backup
            --{,no}preserve --{,no}readahead --cachemem --blend --vt --scroll
            --timeout --{,no}once --resolution --gamma --font --device --mode'
        [[ ${COMPREPLY-} ]] && return
    fi

    # FIXME: It is hard to determine correct supported extensions.
    # fbi can handle any format that imagemagick can plus some others
    _comp_compgen_filedir 'bmp|gif|jp?(e)g|pcd|png|p[pgb]m|tif?(f)|webp|xpm|xwd|?(e)ps|pdf|dvi|txt|svg?(z)|cdr|[ot]tf'
} &&
    complete -F _comp_cmd_fbi fbi

# ex: filetype=sh
