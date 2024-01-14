# cvs(1) completion                                        -*- shell-script -*-

_comp_deprecate_var 2.12 \
    COMP_CVS_REMOTE BASH_COMPLETION_CMD_CVS_REMOTE

# Usage: _comp_cmd_cvs__compgen_entries [base_path]
# @param[opt] $1
# shellcheck disable=SC2120
_comp_cmd_cvs__compgen_entries()
{
    local base_path=${1-$cur}
    local _prefix=${base_path%/*}/
    [[ -e ${_prefix-}CVS/Entries ]] || _prefix=""
    _comp_compgen -c "${cur#"$_prefix"}" split -lP "$_prefix" -- "$(cut -d/ -f2 -s "${_prefix-}CVS/Entries" 2>/dev/null)" &&
        compopt -o filenames
}

_comp_cmd_cvs__modules()
{
    _comp_expand_glob COMPREPLY '"$cvsroot${prefix:+/$prefix}"/!(CVSROOT)'
}

_comp_cmd_cvs__compgen_commands()
{
    _comp_compgen_split -- "$(
        "$1" --help-commands 2>&1 | _comp_awk '/^(     *|\t)/ { print $1 }'
    )"
}

_comp_cmd_cvs__compgen_command_options()
{
    _comp_compgen_help -- --help "$2"
}

_comp_cmd_cvs__compgen_kflags()
{
    _comp_compgen -- -W 'kv kvl k o b v'
}

# @since 2.12
_comp_xfunc_cvs_compgen_roots()
{
    local -a cvsroots=()
    [[ -v CVSROOT ]] && cvsroots=("$CVSROOT")
    [[ -r ~/.cvspass ]] && _comp_split -a cvsroots "$(_comp_awk '{ print $2 }' ~/.cvspass)"
    [[ -r CVS/Root ]] && mapfile -tO "${#cvsroots[@]}" cvsroots <CVS/Root
    ((${#cvsroots[@]})) &&
        _comp_compgen -U cvsroots -- -W '"${cvsroots[@]}"'
    _comp_ltrim_colon_completions "$cur"
}

_comp_deprecate_func 2.12 _cvs_roots _comp_xfunc_cvs_compgen_roots

_comp_cmd_cvs()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    local count mode="" i cvsroot="" has_cvsroot="" pwd
    local -a flags files entries

    local noargopts='!(-*|*[d]*)'
    count=0
    for i in "${words[@]}"; do
        ((count == cword)) && break
        # Last parameter was the CVSROOT, now go back to mode selection
        if [[ ${words[count]} == "${cvsroot-}" && ${mode-} == cvsroot ]]; then
            mode=""
        fi
        if [[ ! $mode ]]; then
            # shellcheck disable=SC2254
            case $i in
                --help | -${noargopts}H)
                    _comp_cmd_cvs__compgen_commands "$1"
                    return
                    ;;
                -${noargopts}d)
                    mode=cvsroot
                    cvsroot=${words[count + 1]}
                    has_cvsroot=set
                    ;;
                add | ad | new)
                    mode=add
                    ;;
                admin | adm | rcs)
                    mode="admin"
                    ;;
                annotate | ann | blame | rannotate | rann | ra)
                    mode=annotate
                    ;;
                checkout | co | get)
                    mode=checkout
                    ;;
                commit | ci | com)
                    mode=commit
                    ;;
                diff | di | dif)
                    mode="diff"
                    ;;
                export | ex | exp)
                    mode="export"
                    ;;
                edit | unedit | editors | logout | pserver | server | watch | watchers)
                    mode=$i
                    ;;
                history | hi | his)
                    mode=history
                    ;;
                import | im | imp)
                    mode=import
                    ;;
                log | lo | rlog | rl)
                    mode=log
                    ;;
                login | logon | lgn)
                    mode=login
                    ;;
                rdiff | patch | pa)
                    mode=rdiff
                    ;;
                release | re | rel)
                    mode=release
                    ;;
                remove | rm | delete)
                    mode=remove
                    ;;
                rtag | rt | rfreeze)
                    mode=rtag
                    ;;
                status | st | stat)
                    mode=status
                    ;;
                tag | ta | freeze)
                    mode=tag
                    ;;
                update | up | upd)
                    mode=update
                    ;;
                version | ve | ver)
                    mode=version
                    ;;
            esac
        elif [[ $i == -* ]]; then
            flags+=("$i")
        fi
        ((count++))
    done

    case ${mode-} in
        add)
            case $prev in
                --*) ;;
                -*m)
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur != -* ]]; then
                _comp_compgen -Rv entries -i cvs entries "${cur-}"
                if [[ ! $cur ]]; then
                    _comp_expand_glob files '!(CVS)'
                else
                    _comp_expand_glob files '"${cur}"*'
                fi
                local f
                for i in "${!files[@]}"; do
                    if [[ ${files[i]} == ?(*/)CVS ]]; then
                        unset -v 'files[i]'
                    elif ((${#entries[@]})); then
                        for f in "${entries[@]}"; do
                            if [[ ${files[i]} == "$f" && ! -d $f ]]; then
                                unset -v 'files[i]'
                                break
                            fi
                        done
                    fi
                done
                # shellcheck disable=SC2154 # global var _comp_backup_glob
                ((${#files[@]})) &&
                    _comp_compgen -- -X "$_comp_backup_glob" -W '"${files[@]}"'
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        admin)
            case $prev in
                --*) ;;
                -*@([aAbcelmnNosu]|t-))
                    return
                    ;;
                -*t)
                    _comp_compgen_filedir
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur == -* ]]; then
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            else
                _comp_cmd_cvs__compgen_entries
            fi
            ;;
        annotate)
            [[ $prev == -[rD] ]] && return

            if [[ $cur == -* ]]; then
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            else
                _comp_cmd_cvs__compgen_entries
            fi
            ;;
        checkout)
            case $prev in
                --*) ;;
                -*[rDj])
                    return
                    ;;
                -*d)
                    _comp_compgen_filedir -d
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur != -* ]]; then
                [[ ! $has_cvsroot ]] && cvsroot=${CVSROOT-}
                _comp_compgen_split -- "$(cvs -d "$cvsroot" co -c 2>/dev/null |
                    _comp_awk '{print $1}')"
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        commit)
            case $prev in
                --*) ;;
                -*[mr])
                    return
                    ;;
                -*F)
                    _comp_compgen_filedir
                    return
                    ;;
            esac

            if [[ $cur != -* ]]; then
                # if $BASH_COMPLETION_CMD_CVS_REMOTE is not null, 'cvs commit'
                # will complete on remotely checked-out files (requires
                # passwordless access to the remote repository
                if [[ ${BASH_COMPLETION_CMD_CVS_REMOTE-} ]]; then
                    # this is the least computationally intensive way found so
                    # far, but other changes (something other than
                    # changed/removed/new) may be missing.
                    _comp_compgen -a split -- "$(cvs -q diff --brief 2>&1 |
                        command sed -ne '
                            # changed
                            s/^Files [^ ]* and \([^ ]*\) differ$/\1/p
                            # new/removed
                            s/^cvs diff: \([^ ]*\) .*, no comparison available$/\1/p
                        ')"
                else
                    _comp_cmd_cvs__compgen_entries
                fi
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        cvsroot)
            _comp_xfunc_cvs_compgen_roots
            ;;
        diff | log | status)
            if [[ $cur == -* ]]; then
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
                [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
            else
                _comp_cmd_cvs__compgen_entries
            fi
            ;;
        editors | watchers)
            if [[ $cur == -* ]]; then
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            else
                _comp_cmd_cvs__compgen_entries
            fi
            ;;
        export)
            case $prev in
                --*) ;;
                -*[rD])
                    return
                    ;;
                -*d)
                    _comp_compgen_filedir -d
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur != -* ]]; then
                [[ ! $has_cvsroot ]] && cvsroot=${CVSROOT-}
                _comp_compgen_split -- "$(cvs -d "$cvsroot" co -c |
                    _comp_awk '{print $1}')"
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        import)
            case $prev in
                --*) ;;
                -*[IbmW])
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur != -* ]]; then
                # starts with same algorithm as checkout
                [[ ! $has_cvsroot ]] && cvsroot=${CVSROOT-}
                local prefix=${cur%/*}
                if [[ -r ${cvsroot}/${prefix} ]]; then
                    _comp_cmd_cvs__modules
                    COMPREPLY=("${COMPREPLY[@]#"$cvsroot"}")
                    COMPREPLY=("${COMPREPLY[@]#\/}")
                fi
                pwd=$(pwd)
                pwd=${pwd##*/}
                [[ $pwd ]] && COMPREPLY+=("$pwd")
                ((${#COMPREPLY[@]})) &&
                    _comp_compgen -- -W '"${COMPREPLY[@]}"'
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        remove)
            if [[ $cur != -* ]]; then
                _comp_compgen -Rv entries -i cvs entries "${cur-}"
                if [[ $prev != -f ]]; then
                    # find out what files are missing
                    for i in "${!entries[@]}"; do
                        [[ -r ${entries[i]} ]] && unset -v 'entries[i]'
                    done
                fi
                ((${#entries[@]})) &&
                    _comp_compgen -- -W '"${entries[@]}"'
            else
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            fi
            ;;
        update)
            case $prev in
                --*) ;;
                -*[rDjIW])
                    return
                    ;;
                -*k)
                    _comp_cmd_cvs__compgen_kflags
                    return
                    ;;
            esac

            if [[ $cur == -* ]]; then
                _comp_cmd_cvs__compgen_command_options "$1" "$mode"
            else
                _comp_cmd_cvs__compgen_entries
            fi
            ;;
        "")
            case $prev in
                --*) ;;
                -*T)
                    _comp_compgen_filedir -d
                    return
                    ;;
                -*[es])
                    return
                    ;;
                -*z)
                    _comp_compgen -- -W '{1..9}'
                    return
                    ;;
            esac

            _comp_compgen_help -- --help-options
            _comp_compgen -a -i cvs commands "$1"
            _comp_compgen -a -- -W \
                "--help --help-commands --help-options --version"
            ;;
    esac

} &&
    complete -F _comp_cmd_cvs cvs

# ex: filetype=sh
