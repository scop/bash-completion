# crontab(1) completion                                    -*- shell-script -*-

_comp_cmd_crontab()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*u)
            _comp_compgen_allowed_users
            return
            ;;
    esac

    local -A opts=([-u]="" [-l]="" [-r]="" [-e]="")
    [[ $OSTYPE == *linux* ]] && opts[-i]=
    [[ -d /sys/fs/selinux || -d /selinux ]] && opts[-s]=

    local i
    for i in "${!words[@]}"; do
        [[ ${words[i]} && $i -ne $cword ]] && unset -v "opts[${words[i]}]"
        case "${words[i]}" in
            -l)
                unset -v 'opts[-r]' 'opts[-e]' 'opts[-i]' 'opts[-s]'
                ;;
            -e)
                unset -v 'opts[-l]' 'opts[-r]' 'opts[-i]'
                ;;
            -r)
                unset -v 'opts[-l]' 'opts[-e]'
                ;;
            -u)
                unset -v 'opts[-i]'
                ;;
        esac
    done

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '"${!opts[@]}"'
        return
    fi

    # do filenames only if we did not have -l, -r, or -e
    [[ ${words[*]} == *\ -[lre]* ]] || _comp_compgen_filedir
} &&
    complete -F _comp_cmd_crontab crontab

# ex: filetype=sh
