# interdiff(1) completion                                  -*- shell-script -*-

_comp_cmd_interdiff()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local noargopts='!(-*|*[Upd]*)'
    # shellcheck disable=SC2254
    case $prev in
        --unified | --strip-match | --drop-context | -${noargopts}[Upd])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local exts='@(?(d)patch|dif?(f))' word
    for word in "${words[@]}"; do
        if [[ $word == -@(z|-decompress) ]]; then
            exts+='?(.@(gz|bz2))'
            break
        fi
    done
    _comp_compgen_filedir "$exts"
} &&
    complete -F _comp_cmd_interdiff interdiff

# ex: filetype=sh
