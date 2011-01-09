# bash completion for GNU make

have make || have gmake || have gnumake || have pmake &&
_make()
{
    local file makef makef_dir="." makef_inc cur prev i split=false

    COMPREPLY=()
    _get_comp_words_by_ref cur prev

    _split_longopt && split=true

    case $prev in
        -f|-o|-W|--file|--makefile|--old-file|--new-file|--assume-old|--assume-new|--what-if)
            _filedir
            return 0
            ;;
        -I|-C|--directory|--include-dir)
            _filedir -d
            return 0
            ;;
    esac

    $split && return 0

    if [[ "$cur" == -* ]]; then
        COMPREPLY=( $( compgen -W '-b -m -B -C -d -e -f -h -i -I\
            -j -l -k -n -o -p -q -r -R - s -S -t -v -w -W \
            --always-make --directory --debug \
            --environment-overrides --file --makefile --help \
            --ignore-errors --include-dir --jobs --load-average \
            --max-load --keep-going --just-print --dry-run \
            --recon --old-file --assume-old --print-data-base \
            --question --no-builtin-rules --no-builtin-variables \
            --silent --quiet --no-keep-goind --stop --touch \
            --version --print-directory --no-print-directory \
            --what-if --new-file --assume-new \
            --warn-undefined-variables' -- "$cur" ) )
    else
        # before we check for makefiles, see if a path was specified
        # with -C/--directory
        for (( i=0; i < ${#COMP_WORDS[@]}; i++ )); do
            if [[ ${COMP_WORDS[i]} == -@(C|-directory) ]]; then
                # eval for tilde expansion
                eval makef_dir=${COMP_WORDS[i+1]}
                break
            fi
        done

        # before we scan for targets, see if a Makefile name was
        # specified with -f/--file/--makefile
        for (( i=0; i < ${#COMP_WORDS[@]}; i++ )); do
            if [[ ${COMP_WORDS[i]} == -@(f|-?(make)file) ]]; then
                # eval for tilde expansion
                eval makef=${COMP_WORDS[i+1]}
                break
            fi
        done

        [ -n "$makef" ] && makef="-f ${makef}"
        [ -n "$makef_dir" ] && makef_dir="-C ${makef_dir}"

        COMPREPLY=( $( compgen -W "$( make -qp $makef $makef_dir 2>/dev/null | \
            awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ \
            {split($1,A,/ /);for(i in A)print A[i]}' )" \
            -- "$cur" ) )

    fi
} &&
complete -F _make make gmake gnumake pmake

# Local variables:
# mode: shell-script
# sh-basic-offset: 4
# sh-indent-comment: t
# indent-tabs-mode: nil
# End:
# ex: ts=4 sw=4 et filetype=sh
