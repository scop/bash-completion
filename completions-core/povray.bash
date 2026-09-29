# povray completion
# by "David Necas (Yeti)" <yeti@physics.muni.cz>

_comp_cmd_povray()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    local oext defoext
    defoext=png # default output extension, if cannot be determined FIXME

    _comp_expand || return

    case $cur in
        [-+]I*)
            _comp_compgen -P "${cur:0:2}" filedir pov
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
            local inputfiles
            if _comp_compgen -Rv inputfiles -- -X '![-+]I*' -W '"${words[@]}"' &&
                _comp_compgen -Rv inputfiles -- -X '' -W '"${inputfiles[@]#[-+]I}"'; then
                local i
                for i in "${!inputfiles[@]}"; do
                    inputfiles[i]=${inputfiles[i]/%.pov/".$oext"}
                done
                _comp_compgen -P "${cur:0:2}" -- -W '"${inputfiles[@]}"'
            fi

            _comp_compgen -aP "${cur:0:2}" filedir "$oext"
            return
            ;;
        *.ini\[ | *.ini\[*[^]]) # sections in .ini files
            [[ $cur =~ ^(.*\.ini)\[ ]] || return
            local ini=${BASH_REMATCH[1]}
            [[ -f $ini && -r $ini ]] || return
            _comp_compgen -P "${ini}[" split -l -- "$(command sed -ne \
                's/^[[:space:]]*\[\([^]]*\]\).*$/\1/p' -- "$ini")"
            # to prevent [bar] expand to nothing.  can be done more easily?
            return
            ;;
        *)
            _comp_compgen_filedir '@(ini|pov)'
            return
            ;;
    esac
} &&
    complete -F _comp_cmd_povray povray xpovray spovray
