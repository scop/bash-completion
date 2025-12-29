# xdg-mime(1) completion                                   -*- shell-script -*-

_comp_cmd_xdg_mime__mimetype()
{
    local d i
    local -a arr
    for d in /usr/share/mime /usr/local/share/mime; do
        _comp_compgen -v arr -C "$d" -- -f -o plusdirs -X "!*.xml" || continue
        for i in "${!arr[@]}"; do
            case ${arr[i]} in
                packages*) unset -v "arr[i]" ;; # not a MIME type dir
                *.xml) arr[i]=${arr[i]%.xml} ;;
                */*) ;;
                *) arr[i]+=/ ;;
            esac
        done
        ((${#arr[@]})) &&
            COMPREPLY+=("${arr[@]}")
    done
    [[ ${COMPREPLY-} != */ ]] || compopt -o nospace
}

_comp_cmd_xdg_mime()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local REPLY
    _comp_count_args
    local args=$REPLY
    if ((args == 1)); then
        if [[ $cur == -* ]]; then
            _comp_compgen -- -W '--help --manual --version'
            return
        fi
        _comp_compgen -- -W 'query default install uninstall'
        return
    fi

    case ${words[1]} in
        query)
            if ((args == 2)); then
                _comp_compgen -- -W 'filetype default'
                return
            fi
            ((args == 3)) || return
            case ${words[2]} in
                filetype) _comp_compgen_filedir ;;
                default) _comp_cmd_xdg_mime__mimetype ;;
            esac
            ;;
        default)
            if ((args == 2)); then
                local -a desktops
                if _comp_expand_glob desktops '/usr/share/applications/*.desktop'; then
                    desktops=("${desktops[@]##*/}")
                    _comp_compgen -- -W '"${desktops[@]}"'
                fi
            else
                _comp_cmd_xdg_mime__mimetype
            fi
            ;;
        install)
            if [[ $cur == -* ]]; then
                _comp_compgen -- -W '--mode --novendor'
            elif [[ $prev == --mode ]]; then
                _comp_compgen -- -W 'user system'
            else
                _comp_compgen_filedir xml
            fi
            ;;
        uninstall)
            if [[ $cur == -* ]]; then
                _comp_compgen -- -W '--mode'
            elif [[ $prev == --mode ]]; then
                _comp_compgen -- -W 'user system'
            else
                _comp_compgen_filedir xml
            fi
            ;;
    esac
} &&
    complete -F _comp_cmd_xdg_mime xdg-mime

# ex: filetype=sh
