# bash completion for info                                 -*- shell-script -*-

_comp_cmd_info()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    # default completion if parameter looks like a path
    if [[ $cur == @(*/|[.~])* ]]; then
        _comp_compgen_filedir
        return
    fi

    local noargopts='!(-*|*[kndfor]*)'
    # shellcheck disable=SC2254
    case $prev in
        --apropos | --index-search | --node | --help | --version | -${noargopts}[knhv])
            return
            ;;
        -${noargopts}d)
            if [[ ${1##*/} == info ]]; then
                _comp_compgen_filedir -d
                return
            fi
            ;;
        --directory)
            _comp_compgen_filedir -d
            return
            ;;
        --dribble | --file | --output | --restore | --raw-filename | --rcfile | -${noargopts}[for])
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    local i infopath=/usr/share/info

    if [[ ${INFOPATH-} == *: ]]; then
        infopath=${INFOPATH}${infopath}
    elif [[ ${INFOPATH:+set} ]]; then
        infopath=$INFOPATH
    fi

    _comp_split -F : infopath "$infopath"
    if ((${#infopath[@]})); then
        _comp_compgen -Rv infopath -- -S "/$cur*" -W '"${infopath[@]}"'
        local IFS=
        if _comp_expand_glob COMPREPLY '${infopath[@]}'; then
            # weed out directory path names and paths to info pages (empty
            # elements will be removed by the later `compgen -X ''`)
            COMPREPLY=("${COMPREPLY[@]##*/?(:)}")
            # strip suffix from info pages
            COMPREPLY=("${COMPREPLY[@]%.@(gz|bz2|xz|lzma)}")
            # weed out info dir file with -X 'dir'
            _comp_compgen -c "${cur//\\\\/}" -- -W '"${COMPREPLY[@]%.*}"' -X '@(|dir)'
        fi
        _comp_unlocal IFS
    fi
} &&
    complete -F _comp_cmd_info info pinfo

# ex: filetype=sh
