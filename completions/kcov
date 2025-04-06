# kcov(1) completion                                       -*- shell-script -*-

_comp_cmd_kcov()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -n : -- "$@" || return

    case "$prev" in
        --pid | -p)
            _comp_compgen_pids
            return
            ;;
        --sort-type | -s)
            _comp_compgen -- -W 'filename percent reverse lines uncovered'
            return
            ;;
        --include-path | --exclude-path)
            _comp_compgen_filedir
            return
            ;;
        --replace-src-path)
            if [[ $cur == ?*:* ]]; then
                _comp_compgen -c "${cur##*:}" filedir
            else
                _comp_compgen_filedir
                compopt -o nospace
            fi
            return
            ;;
        --limits | -l)
            # Complete the option argument of the form "--limits low,high".
            local prefix
            if [[ $cur =~ ^.+, ]]; then
                prefix=$BASH_REMATCH
            else
                prefix=""
                compopt -o nospace
            fi
            _comp_compgen -P "$prefix" -- -W "{0..100}" &&
                if ((${#COMPREPLY[@]} == 1)); then
                    # When we complete the "low" part, we suffix a comma.
                    [[ $prefix ]] || COMPREPLY=("${COMPREPLY[@]/%/,}")
                else
                    # When the result is not unique, we do not show the prefix
                    # part on the list.
                    COMPREPLY=("${COMPREPLY[@]##*,}")
                fi
            return
            ;;
        --title | -t | --include-pattern | --exclude-pattern | --path-strip-level)
            # argument required but no completions available
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_kcov kcov

# ex: filetype=sh
