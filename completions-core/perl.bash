# bash completion for perl                                 -*- shell-script -*-

_comp_cmd_perl__helper()
{
    _comp_compgen_split -P "$prefix" -- "$("${1:-perl}" \
        "${BASH_SOURCE[0]%/*}/../helpers/perl" "$2" "$cur")"
    [[ $2 == functions ]] || _comp_ltrim_colon_completions "$prefix$cur"
}

_comp_cmd_perl()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    local prefix="" temp optPrefix optSuffix

    # If option not followed by whitespace, reassign prev and cur
    if [[ $cur == -?* ]]; then
        temp=$cur
        prev=${temp:0:2}
        cur=${temp:2}
        if [[ $prev == -d && $cur == t* ]]; then
            prev=-dt
            cur=${cur:1}
        fi
        optPrefix=-P$prev
        optSuffix=-S/
        prefix=$prev

        case $prev in
            -*[DeEiFl])
                return
                ;;
            -*[Ix])
                compopt -o filenames
                _comp_compgen -- -d "$optPrefix" $optSuffix
                return
                ;;
            -*[mM])
                temp="${cur#-}"
                prefix+=${cur%"$temp"}
                cur="$temp"
                _comp_cmd_perl__helper "$1" modules
                return
                ;;
            -*V)
                if [[ $cur == :* ]]; then
                    temp="${cur##+(:)}"
                    prefix+=${cur%"$temp"}
                    _comp_compgen -c "$temp" split -lP "$prefix" -- "$(
                        "$1" -MConfig -e 'print join "\n",
                           keys %Config::Config' 2>/dev/null
                    )"
                    _comp_ltrim_colon_completions "$prefix$temp"
                fi
                return
                ;;
            -*d | -*dt)
                if [[ $cur == :* ]]; then
                    temp="${cur#:}"
                    prefix=$prefix${cur%"$temp"}
                    cur="Devel::$temp"
                    _comp_cmd_perl__helper "$1" modules
                fi
                ;;
        esac

    # Unlike other perl options, having a space between the `-e' and
    # `-E' options and their arguments, e.g. `perl -e "exit 2"', is
    # valid syntax.  However, the argument is neither a filename nor a
    # directory, but one line of perl program, thus do not suggest
    # _comp_compgen_filedir completion.
    elif [[ $prev == -e ]] || [[ $prev == -E ]]; then
        return

    # Likewise, `-I' also accepts a space between option and argument
    # and it takes a directory as value.
    elif [[ $prev == -I ]]; then
        compopt -o filenames
        # shellcheck disable=SC2086
        _comp_compgen -- -d ${optPrefix-} ${optSuffix-}
        return

    elif [[ $cur == -* ]]; then
        _comp_compgen -- -W '-C -s -T -u -U -W -X -h -v -V -c -w -d -D -p -n -a
            -F -l -0 -I -m -M -P -S -x -i -e'
    else
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_perl perl

_comp_cmd_perldoc()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    local prefix="" temp

    # completing an option (may or may not be separated by a space)
    if [[ $cur == -?* ]]; then
        temp=$cur
        prev=${temp:0:2}
        cur=${temp:2}
        prefix=$prev
    fi

    # Prefer `perl` in the same dir in utility functions
    local pathcmd
    pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH

    case $prev in
        -*[hVnoMwL])
            return
            ;;
        -*d)
            _comp_compgen_filedir
            return
            ;;
        -*f)
            _comp_cmd_perl__helper "" functions
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
    else
        # return available modules (unless it is clearly a file)
        if [[ $cur != @(*/|[.~])* ]]; then
            _comp_cmd_perl__helper "" perldocs
            if [[ $cur == p* ]]; then
                _comp_compgen -a split -- "$(PERLDOC_PAGER=cat "$1" -u perl |
                    command sed -ne '/perl.*Perl overview/,/perlwin32/p' |
                    _comp_awk 'NF >= 2 && $1 ~ /^perl/ { print $1 }')"
            fi
        fi
        _comp_compgen -a filedir 'p@([lm]|od)'
    fi
} &&
    complete -F _comp_cmd_perldoc -o bashdefault perldoc

# ex: filetype=sh
