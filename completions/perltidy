# perltidy(1) completion                                   -*- shell-script -*-

_comp_cmd_perltidy()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    case $prev in
        -h | --help)
            return
            ;;
        -o)
            _comp_compgen_filedir
            return
            ;;
    esac

    case $cur in
        -pro=* | --profile=*)
            _comp_compgen -c "${cur#*=}" filedir
            return
            ;;
        -ole=* | --output-line-ending=*)
            _comp_compgen -c "${cur#*=}" -- -W 'dos win mac unix'
            return
            ;;
        -bt=* | --brace-tightness=* | -pt=* | --paren-tightness=* | \
            -sbt=* | --square-bracket-tightness=* | \
            -bvt=* | --brace-vertical-tightness=* | \
            -pvt=* | --paren-vertical-tightness=* | \
            -sbvt=* | --square-bracket-vertical-tightness=* | \
            -bvtc=* | --brace-vertical-tightness-closing=* | \
            -pvtc=* | --paren-vertical-tightness-closing=* | \
            -sbvtc=* | --square-bracket-vertical-tightness-closing=* | \
            -cti=* | --closing-token-indentation=* | \
            -kbl=* | --keep-old-blank-lines=* | \
            -vt=* | --vertical-tightness=*)
            _comp_compgen -c "${cur#*=}" -- -W '0 1 2'
            return
            ;;
        -vtc=* | --vertical-tightness-closing=*)
            _comp_compgen -c "${cur#*=}" -- -W '0 1'
            return
            ;;
        -cab=* | --comma-arrow-breakpoints=*)
            _comp_compgen -c "${cur#*=}" -- -W '0 1 2 3'
            return
            ;;
        -*=)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen_filedir 'p[lm]|t'
    fi
} &&
    complete -F _comp_cmd_perltidy perltidy

# ex: filetype=sh
