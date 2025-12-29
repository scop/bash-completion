# lz4 completion                                           -*- shell-script -*-

_comp_cmd_lz4()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -b)
            _comp_compgen_filedir
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -R help -- -h
        _comp_compgen -- -X '-*#*' -W \
            '${COMPREPLY+"${COMPREPLY[@]}"} -B{4..7} -i{1..9}'
        return
    fi

    local REPLY word xspec="*.?(t)lz4"
    _comp_count_args
    local args=$REPLY
    ((args > 2)) && return

    for word in "${words[@]}"; do
        case $word in
            -*[dt]*)
                case $args in
                    1) xspec="!"$xspec ;;
                    2) [[ $word == *t* ]] && return ;;
                esac
                break
                ;;
            -z)
                case $args in
                    1) xspec= ;;
                    2) xspec="!"$xspec ;;
                esac
                break
                ;;
        esac
    done

    _comp_compgen_tilde && return

    compopt -o filenames
    _comp_compgen -- -f -X "$xspec" -o plusdirs
} &&
    complete -F _comp_cmd_lz4 lz4 lz4c

# ex: filetype=sh
