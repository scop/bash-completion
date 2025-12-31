# bash completion for rdesktop                             -*- shell-script -*-

_comp_cmd_rdesktop()
{
    local cur prev words cword comp_args
    _comp_initialize -n : -- "$@" || return

    case $prev in
        -*k)
            _comp_expand_glob COMPREPLY '/usr/share/rdesktop/keymaps/!(*@(common|modifiers)*) {"$HOME/.rdesktop",.}/keymaps/*' &&
                _comp_compgen -- -W '"${COMPREPLY[@]}"'
            return
            ;;
        -*a)
            _comp_compgen -- -W '8 15 16 24'
            return
            ;;
        -*x)
            _comp_compgen -- -W 'broadband modem lan'
            return
            ;;
        -*r)
            case $cur in
                sound:*)
                    _comp_compgen -c "${cur#sound:}" -- -W 'local off remote'
                    ;;
                *:*) ;;

                *)
                    _comp_compgen -- -W 'comport: disk: lptport: printer:
                        sound: lspci scard'
                    [[ ${COMPREPLY-} == *: ]] && compopt -o nospace
                    ;;
            esac
            return
            ;;
        -*[udscpngSTX])
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        local -a opts
        _comp_compgen -Rv opts help
        ((${#opts[@]})) &&
            _comp_compgen -- -W '"${opts[@]%:}"'
    else
        _comp_compgen_known_hosts -- "$cur"
    fi

} &&
    complete -F _comp_cmd_rdesktop rdesktop

# ex: filetype=sh
