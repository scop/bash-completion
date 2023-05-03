# bash completion for fbgs(1)                              -*- shell-script -*-

_comp_cmd_fbgs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case "$prev" in
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
        -fp | --firstpage | -lp | --lastpage | -r | --resolution | -s | --scroll | -t | \
            --timeout)
            # expect integer value
            _comp_compgen -aR -- -W '{0..9}'
            compopt -o nospace
            return
            ;;
        -T | --vt | -p | --password | -g | --gamma)
            # argument required but no completions available
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--bell --help --password -fp --firstpage -lp
            --lastpage --color -l -xl -xxl --resolution --autozoom
            --{,no}autoup --{,no}autodown --{,no}fitwidth --{,no}verbose
            --{,no}random --vt --scroll --timeout --{,no}once --gamma --font
            --device --mode'
        [[ ${COMPREPLY-} ]] && return
    fi

    _comp_compgen_filedir '?(e)ps|pdf'
} &&
    complete -F _comp_cmd_fbgs fbgs

# ex: filetype=sh
