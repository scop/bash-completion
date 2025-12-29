# bash completion for sudo(8)                              -*- shell-script -*-

_comp_cmd_sudo()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local i mode=normal
    [[ $1 == *sudoedit ]] && mode=edit

    local noargopts='!(-*|*[CDghpRrTtUu]*)'
    [[ $mode == normal ]] &&
        for ((i = 1; i <= cword; i++)); do
            if [[ ${words[i]} != -* ]]; then
                local PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin
                local _comp_root_command=$1
                _comp_command_offset $i
                return
            fi
            # shellcheck disable=SC2254
            if [[ ${words[i]} == -@(${noargopts}e*|-edit) ]]; then
                mode=edit
                break
            fi
            # shellcheck disable=SC2254
            [[ ${words[i]} == @(--@(close-from|chdir|group|host|prompt|chroot|role|command-timeout|type|other-user|user)|-${noargopts}[CDghpRrTtUu]) ]] &&
                ((i++))
        done

    # shellcheck disable=SC2254
    case "$prev" in
        --user | --other-user | -${noargopts}[uU])
            _comp_compgen -- -u
            return
            ;;
        --group | -${noargopts}g)
            _comp_compgen -- -g
            return
            ;;
        --close-from | --prompt | --role | --type | --command-timeout | \
            -${noargopts}[CprTt])
            return
            ;;
        --chdir | --chroot | -${noargopts}[DR])
            _comp_compgen_filedir -d
            return
            ;;
        --host | -${noargopts}h)
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen_help || _comp_compgen_usage
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
        return
    fi
    if [[ $mode == edit ]]; then
        _comp_compgen_filedir
    fi
} &&
    complete -F _comp_cmd_sudo sudo sudoedit sudo.ws sudo-rs

# ex: filetype=sh
