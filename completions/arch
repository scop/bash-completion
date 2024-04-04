# mailman arch completion                                  -*- shell-script -*-

# Try to detect whether this is the mailman "arch" to avoid installing
# it for the coreutils/util-linux-ng one.
_comp_have_command mailmanctl &&
    _comp_cmd_arch()
    {
        local cur prev words cword was_split comp_args
        _comp_initialize -s -- "$@" || return

        case $prev in
            -w | -g | -d | --welcome-msg | --goodbye-msg | --digest)
                _comp_compgen -- -W 'y n'
                return
                ;;
            --file)
                _comp_compgen_filedir
                return
                ;;
        esac

        [[ $was_split ]] && return

        if [[ $cur == -* ]]; then
            _comp_compgen_help
        else
            local args=$cword
            for ((i = 1; i < cword; i++)); do
                if [[ ${words[i]} == -* ]]; then
                    ((args--))
                fi
            done
            case $args in
                1)
                    # Prefer `list_lists` in the same dir as command
                    local pathcmd
                    pathcmd=$(type -P -- "$1") && local PATH=${pathcmd%/*}:$PATH
                    _comp_compgen -x list_lists mailman_lists
                    ;;
                2)
                    _comp_compgen_filedir
                    ;;
            esac
        fi

    } &&
        complete -F _comp_cmd_arch arch

# ex: filetype=sh
