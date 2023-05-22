# isort completion                                         -*- shell-script -*-

_comp_cmd_isort()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --add-import | --builtin | --future | --from-first | -ff | \
            --force-grid-wrap | -fgw | --indent | --lines | --lines-after-imports | -lai | \
            --lines-between-types | -lbt | --line-ending | -le | --no-lines-before | -nlb | \
            --dont-skip | -ns | --thirdparty | --project | --remove-import | --skip | \
            --skip-glob | -sg | --settings-path | -sp | --top | --virtual-env | --line-width | \
            --wrap-length | -wl | -[habfiloprstw])
            return
            ;;
        --jobs | -j)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "{1..$REPLY}"
            return
            ;;
        --multi-line | -m)
            _comp_compgen -- -W '{0..5}'
            return
            ;;
        --section-default | -sd)
            _comp_compgen -- -W 'FUTURE STDLIB THIRDPARTY FIRSTPARTY
                LOCALFOLDER'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir '@(py|pyi)'
} &&
    complete -F _comp_cmd_isort isort

# ex: filetype=sh
