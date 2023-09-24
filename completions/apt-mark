# Debian apt-mark(8) completion                            -*- shell-script -*-

_comp_cmd_apt_mark()
{
    local cur prev words cword was_split comp_args
    _comp_initialize -s -- "$@" || return

    local special="" i
    for ((i = 1; i < cword; i++)); do
        if [[ ${words[i]} == @(auto|manual|minimize-manual|showauto|showmanual|hold|unhold|showhold|install|remove|deinstall|purge|showinstall|showremove|showpurge) ]]; then
            special=${words[i]}
            break
        fi
    done

    if [[ $special ]]; then
        case $special in
            auto | manual | unhold)
                local -A showcmds=([auto]=manual [manual]=auto [unhold]=hold)
                local showcmd=${showcmds[$special]}
                _comp_compgen_split -- "$("$1" "show$showcmd" 2>/dev/null)"
                return
                ;;
            minimize-manual)
                return
                ;;
            *)
                _comp_compgen -x apt-get installed_packages
                ;;
        esac
        return
    fi

    local noargopts='!(-*|*[ocf]*)'
    # shellcheck disable=SC2254
    case $prev in
        --help | --version | --option | -${noargopts}[hvo])
            return
            ;;
        --config-file | -${noargopts}c)
            _comp_compgen_filedir conf
            return
            ;;
        --file | -${noargopts}f)
            _comp_compgen_filedir
            return
            ;;
    esac

    [[ $was_split ]] && return

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '--file= --help --version --config-file --option'
        [[ ${COMPREPLY-} == *= ]] && compopt -o nospace
    else
        _comp_compgen -- -W 'auto manual minimize-manual showauto showmanual
            hold unhold showhold install remove purge showinstall showremove
            showpurge'
    fi

} &&
    complete -F _comp_cmd_apt_mark apt-mark

# ex: filetype=sh
