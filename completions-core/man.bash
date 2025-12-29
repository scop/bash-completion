# man(1) completion                                        -*- shell-script -*-

_comp_cmd_man()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    local comprsuffix=".@([glx]z|bz2|lzma|Z|zst)"
    local manext="@([0-9]*([a-z])|[lnp]|man)?($comprsuffix)"
    local mansect="@([0-9]*([a-z])|[lnp])"

    local noargopts='!(-*|*[ClMSsPpLmerRE]*)'
    # shellcheck disable=SC2254
    case $prev in
        --config-file | -${noargopts}C)
            _comp_compgen_filedir conf
            return
            ;;
        --local-file | -${noargopts}l)
            _comp_compgen_filedir "$manext"
            return
            ;;
        --manpath | -${noargopts}M)
            _comp_compgen_filedir -d
            return
            ;;
        --sections | -${noargopts}[Ss])
            _comp_delimited : -W '{1..9}'
            return
            ;;
        --pager | -${noargopts}P)
            _comp_compgen_commands
            return
            ;;
        --preprocessor | -${noargopts}p)
            _comp_compgen -- -W 'e p t g r v'
            return
            ;;
        --locale | --systems | --extension | --prompt | --recode | --encoding | \
            -${noargopts}[LmerRE])
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h || _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    # file based completion if parameter looks like a path
    if _comp_looks_like_path "$cur"; then
        _comp_compgen_filedir "$manext"
        return
    fi

    local manpath=$(manpath 2>/dev/null || command man -w 2>/dev/null)
    if [[ ! $manpath ]]; then
        # Note: Both "manpath" and "man -w" may be unavailable, in
        # which case we determine the man paths based on the
        # environment variable MANPATH.
        manpath=:${MANPATH-}:
        # Note: An empty path (represented by two consecutive colons
        # or a preceding/trailing colon) represents the system man
        # paths.
        manpath=${manpath//::/':/usr/share/man:/usr/local/share/man:'}
        manpath=${manpath:1:-1}
    fi

    # determine manual section to search
    local sect
    # shellcheck disable=SC2053
    [[ $prev == $mansect ]] && sect=$prev || sect='*'

    _comp_split -F : manpath "$manpath"
    if ((${#manpath[@]})); then
        local manfiles
        _comp_compgen -Rv manfiles -- -S "/*man$sect/$cur*" -W '"${manpath[@]}"'
        _comp_compgen -aRv manfiles -- -S "/*cat$sect/$cur*" -W '"${manpath[@]}"'

        local IFS=
        if _comp_expand_glob COMPREPLY '${manfiles[@]}'; then
            # weed out directory path names and paths to man pages (empty
            # elements will be removed by the later `compgen -X ''`)
            COMPREPLY=("${COMPREPLY[@]##*/?(:)}")
            # strip suffix from man pages
            COMPREPLY=("${COMPREPLY[@]%$comprsuffix}")
            _comp_compgen -c "${cur//\\\\/}" -- -W '"${COMPREPLY[@]%.*}"' -X ''
        fi
        _comp_unlocal IFS
    fi

    # shellcheck disable=SC2053
    if [[ $prev != $mansect ]]; then
        # File based completion for the rest, prepending ./ if needed
        # (man 1.6f needs that for man pages in current dir)
        local i start=${#COMPREPLY[@]}
        _comp_compgen -a filedir "$manext"
        for ((i = start; i < ${#COMPREPLY[@]}; i++)); do
            [[ ${COMPREPLY[i]} == */* ]] || COMPREPLY[i]=./${COMPREPLY[i]}
        done
    fi

    _comp_ltrim_colon_completions "$cur"
} &&
    complete -F _comp_cmd_man man apropos whatis

# ex: filetype=sh
