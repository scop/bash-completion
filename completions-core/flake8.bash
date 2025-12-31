# flake8 completion                                        -*- shell-script -*-

_comp_cmd_flake8()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[j]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | -${noargopts}h)
            return
            ;;
        --format)
            _comp_compgen -- -W 'default pylint'
            return
            ;;
        --jobs | -${noargopts}j)
            local REPLY
            _comp_get_ncpus
            _comp_compgen -- -W "auto {1..$REPLY}"
            return
            ;;
        --output-file | --append-config | --config)
            _comp_compgen_filedir
            return
            ;;
        --include-in-doctest | --exclude-from-doctest)
            _comp_compgen_filedir py
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir py
} &&
    complete -F _comp_cmd_flake8 flake8

# ex: filetype=sh
