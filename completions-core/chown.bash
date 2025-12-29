# chown(1) completion                                      -*- shell-script -*-

_comp_cmd_chown()
{
    local cur prev words cword was_split comp_args
    # Don't treat user:group as separate words.
    _comp_initialize -s -n : -- "$@" || return

    case "$prev" in
        --from)
            _comp_compgen_usergroups
            return
            ;;
        --reference)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        # Complete -options
        local w opts=""
        for w in "${words[@]}"; do
            [[ $w == -@(R|-recursive) ]] && opts="-H -L -P" && break
        done
        _comp_compgen -- -W '-c -h -f -R -v --changes --dereference
            --no-dereference --from --silent --quiet --reference --recursive
            --verbose --help --version $opts'
    else
        local REPLY

        # The first argument is a usergroup; the rest are filedir.
        _comp_count_args

        if ((REPLY == 1)); then
            _comp_compgen_usergroups -u
        else
            _comp_compgen_filedir
        fi
    fi
} &&
    complete -F _comp_cmd_chown chown

# ex: filetype=sh
