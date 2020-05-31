# bash completion for GNU make                             -*- shell-script -*-

_make_target_extract_script()
{
    local mode="$1"
    shift

    local prefix="$1"
    local prefix_pat=$(command sed 's/[][\,.*^$(){}?+|/]/\\&/g' <<<"$prefix")
    local basename=${prefix##*/}
    local dirname_len=$((${#prefix} - ${#basename}))

    if [[ $mode == -d ]]; then
        # display mode, only output current path component to the next slash
        local output="\2"
    else
        # completion mode, output full path to the next slash
        local output="\1\2"
    fi

    cat <<EOF
    1,/^# * Make data base/           d;        # skip any makefile output
    /^# * Finished Make data base/,/^# * Make data base/{
                                      d;        # skip any makefile output
    }
    /^# * Variables/,/^# * Files/     d;        # skip until files section
    /^# * Not a target/,/^$/          d;        # skip not target blocks
    /^${prefix_pat}/,/^$/!            d;        # skip anything user dont want

    # The stuff above here describes lines that are not
    #  explicit targets or not targets other than special ones
    # The stuff below here decides whether an explicit target
    #  should be output.

    /^# * File is an intermediate prerequisite/ {
      s/^.*$//;x;                               # unhold target
      d;                                        # delete line
    }

    /^$/ {                                      # end of target block
      x;                                        # unhold target
      /^$/d;                                    # dont print blanks
      s|^\(.\{${dirname_len}\}\)\(.\{${#basename}\}[^:/]*/\{0,1\}\)[^:]*:.*$|${output}|p;
      d;                                        # hide any bugs
    }

    # This pattern includes a literal tab character as \t is not a portable
    # representation and fails with BSD sed
    /^[^#	:%]\{1,\}:/ {         # found target block
      /^\.PHONY:/                 d;            # special target
      /^\.SUFFIXES:/              d;            # special target
      /^\.DEFAULT:/               d;            # special target
      /^\.PRECIOUS:/              d;            # special target
      /^\.INTERMEDIATE:/          d;            # special target
      /^\.SECONDARY:/             d;            # special target
      /^\.SECONDEXPANSION:/       d;            # special target
      /^\.DELETE_ON_ERROR:/       d;            # special target
      /^\.IGNORE:/                d;            # special target
      /^\.LOW_RESOLUTION_TIME:/   d;            # special target
      /^\.SILENT:/                d;            # special target
      /^\.EXPORT_ALL_VARIABLES:/  d;            # special target
      /^\.NOTPARALLEL:/           d;            # special target
      /^\.ONESHELL:/              d;            # special target
      /^\.POSIX:/                 d;            # special target
      /^\.NOEXPORT:/              d;            # special target
      /^\.MAKE:/                  d;            # special target
EOF

    # don't complete with hidden targets unless we are doing a partial completion
    if [[ -z ${prefix_pat} || ${prefix_pat} == */ ]]; then
        cat <<EOF
      /^${prefix_pat}[^a-zA-Z0-9]/d;            # convention for hidden tgt
EOF
    fi

    cat <<EOF
      h;                                        # hold target
      d;                                        # delete line
    }

EOF
}

_make()
{
    local cur prev words cword split
    _init_completion -s || return

    local makef makef_dir=("-C" ".") i

    case $prev in
        --file | --makefile | --old-file | --assume-old | --what-if | --new-file | \
            --assume-new | -!(-*)[foW])
            _filedir
            return
            ;;
        --include-dir | --directory | -!(-*)[ICm])
            _filedir -d
            return
            ;;
        -!(-*)E)
            COMPREPLY=($(compgen -v -- "$cur"))
            return
            ;;
        --eval | -!(-*)[DVx])
            return
            ;;
        --jobs | -!(-*)j)
            COMPREPLY=($(compgen -W "{1..$(($(_ncpus) * 2))}" -- "$cur"))
            return
            ;;
    esac

    $split && return

    if [[ $cur == -* ]]; then
        local opts="$(_parse_help "$1")"
        COMPREPLY=($(compgen -W '${opts:-$(_parse_usage "$1")}' -- "$cur"))
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    elif [[ $cur == *=* ]]; then
        prev=${cur%%=*}
        cur=${cur#*=}
        local diropt
        [[ ${prev,,} == *dir?(ectory) ]] && diropt=-d
        _filedir $diropt
    else
        # before we check for makefiles, see if a path was specified
        # with -C/--directory
        for ((i = 1; i < ${#words[@]}; i++)); do
            if [[ ${words[i]} == -@(C|-directory) ]]; then
                # eval for tilde expansion
                eval "makef_dir=( -C \"${words[i + 1]}\" )"
                break
            fi
        done

        # before we scan for targets, see if a Makefile name was
        # specified with -f/--file/--makefile
        for ((i = 1; i < ${#words[@]}; i++)); do
            if [[ ${words[i]} == -@(f|-?(make)file) ]]; then
                # eval for tilde expansion
                eval "makef=( -f \"${words[i + 1]}\" )"
                break
            fi
        done

        # recognise that possible completions are only going to be displayed
        # so only the base name is shown
        local mode=--
        if ((COMP_TYPE != 9)); then
            mode=-d # display-only mode
        fi

        local IFS=$' \t\n' script=$(_make_target_extract_script $mode "$cur")
        COMPREPLY=($(LC_ALL=C \
            $1 -npq __BASH_MAKE_COMPLETION__=1 \
            ${makef+"${makef[@]}"} "${makef_dir[@]}" .DEFAULT 2>/dev/null |
            command sed -ne "$script"))

        if [[ $mode != -d ]]; then
            # Completion will occur if there is only one suggestion
            # so set options for completion based on the first one
            [[ ${COMPREPLY-} == */ ]] && compopt -o nospace
        fi

    fi
} &&
    complete -F _make make gmake gnumake pmake colormake bmake

# ex: filetype=sh
