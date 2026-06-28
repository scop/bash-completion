# povray completion
# by "David Necas (Yeti)" <yeti@physics.muni.cz>

_comp_cmd_povray()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local povcur=$cur pfx oext defoext
    defoext=png # default output extension, if cannot be determined FIXME

    _comp_expand || return

    case $povcur in
        [-+]I*)
            cur="${povcur#[-+]I}" # to confuse _comp_compgen_filedir
            pfx="${povcur%"$cur"}"
            _comp_compgen_filedir pov &&
                _comp_compgen -Rv COMPREPLY -- -P "$pfx" -W '"${COMPREPLY[@]}"'
            return
            ;;
        [-+]O*)
            # guess what output file type user may want
            local IFS=$'\n'
            case "$IFS${words[*]}" in
                *"$IFS"[-+]FN*) oext=png ;;
                *"$IFS"[-+]FP*) oext=ppm ;;
                *"$IFS"[-+]F[CT]*) oext=tga ;;
                *) oext=$defoext ;;
            esac
            _comp_unlocal IFS
            # complete filename corresponding to previously specified +I
            if _comp_compgen -Rv COMPREPLY -- -X '![-+]I*' -W '"${words[@]}"' &&
                _comp_compgen -Rv COMPREPLY -- -X '' -W '"${COMPREPLY[@]#[-+]I}"'; then
                local i
                for i in "${!COMPREPLY[@]}"; do
                    COMPREPLY[i]=${COMPREPLY[i]/%.pov/".$oext"}
                done
            fi
            cur="${povcur#[-+]O}" # to confuse _comp_compgen_filedir
            pfx="${povcur%"$cur"}"
            _comp_compgen -a filedir "$oext"
            ((${#COMPREPLY[@]})) &&
                _comp_compgen -Rv COMPREPLY -- -P "$pfx" -W '"${COMPREPLY[@]}"'
            return
            ;;
        *.ini\[ | *.ini\[*[^]]) # sections in .ini files
            cur="${povcur#*\[}"
            pfx="${povcur%\["$cur"}" # prefix == filename
            [[ -f $pfx && -r $pfx ]] || return
            _comp_compgen_split -l -- "$(command sed -ne \
                's/^[[:space:]]*\[\([^]]*\]\).*$/\1/p' -- "$pfx")" &&
                # to prevent [bar] expand to nothing.  can be done more easily?
                _comp_compgen -Rv COMPREPLY -- -P "${pfx}[" -W '"${COMPREPLY[@]}"'
            return
            ;;
        *)
            _comp_compgen_filedir '@(ini|pov)'
            return
            ;;
    esac
} &&
    complete -F _comp_cmd_povray povray xpovray spovray
