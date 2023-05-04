# Gnatmake completion                                      -*- shell-script -*-
# by Ralf_Schroth@t-online.de (Ralf Schroth)

_comp_cmd_gnatmake()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    if [[ $cur == -* ]]; then
        # relevant (and less relevant ;-) )options completion
        _comp_compgen -- -W '-a -c -f -i -j -k -m -M -n -o -q -s -v -z -aL -A
            -aO -aI -I -I- -L -nostdinc -nostdlib -cargs -bargs -largs
            -fstack-check -fno-inline -g -O1 -O0 -O2 -O3 -gnata -gnatA -gnatb
            -gnatc -gnatd -gnatD -gnate -gnatE -gnatf -gnatF -gnatg -gnatG
            -gnath -gnati -gnatk -gnatl -gnatL -gnatm -gnatn -gnato -gnatO
            -gnatp -gnatP -gnatq -gnatR -gnats -gnatt -gnatT -gnatu -gnatU
            -gnatv -gnatws -gnatwe -gnatwl -gnatwu -gnatW -gnatx -gnatX -gnaty
            -gnatz -gnatZ -gnat83'
    else
        # source file completion
        _comp_compgen_filedir '@(adb|ads)'
    fi
} &&
    complete -F _comp_cmd_gnatmake gnatmake

# ex: filetype=sh
