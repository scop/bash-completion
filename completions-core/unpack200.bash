# unpack200(1) completion                                  -*- shell-script -*-

_comp_cmd_unpack200()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[Hl]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}[?hVJ])
            return
            ;;
        --deflate-hint | -${noargopts}H)
            _comp_compgen -- -W 'true false keep'
            return
            ;;
        --log-file | -${noargopts}l)
            _comp_compgen -- -W '-'
            _comp_compgen -a filedir log
            return
            ;;
    esac

    [[ $was_split ]] && return

    # Check if a pack or a jar was already given.
    local word pack="" jar=""
    for word in "${words[@]:1}"; do
        case $word in
            *.pack | *.pack.gz) pack=set ;;
            *.jar) jar=set ;;
        esac
    done

    if [[ ! $pack ]]; then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--deflate-hint= --remove-pack-file --verbose
                --quiet --log-file= --help --version'
            [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        else
            _comp_compgen_filedir 'pack?(.gz)'
        fi
    elif [[ ! $jar ]]; then
        _comp_compgen_filedir jar
    fi
} &&
    complete -F _comp_cmd_unpack200 unpack200

# ex: filetype=sh
