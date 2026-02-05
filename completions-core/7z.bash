# 7z(1) completion                                         -*- shell-script -*-

_comp_cmd_7z()
{
    local cur prev words cword comp_args
    _comp_initialize -n = -- "$@" || return

    if ((cword == 1)); then
        _comp_compgen -- -W 'a b d e h i l rn t u x'
        return
    fi

    local mode
    [[ ${words[1]} == @(a|d|rn|u) ]] && mode=w || mode=r

    case $cur in
        -ao*)
            _comp_compgen -P "-ao" -- -W 'a s t u'
            return
            ;;
        -?(a)[ix]*)
            if [[ $cur != *[@\!]* ]]; then
                [[ $cur =~ ^-a?[ix] ]]
                local prefix=${BASH_REMATCH-}
                _comp_compgen -P "$prefix" -- -W '@ ! r@ r-@ r0@ r! r-! r0!'
            elif [[ $cur =~ ^-a?[ix](r|r-|r0)?@ ]]; then
                local prefix=${BASH_REMATCH-}
                _comp_compgen -P "$prefix" -- -f
                compopt -o filenames
            fi
            return
            ;;
        -mhe=* | -mhc=* | -ms=* | -mt=*)
            _comp_compgen -c "${cur#*=}" -- -W 'on off'
            return
            ;;
        -mx=*)
            _comp_compgen -c "${cur#*=}" -- -W '0 1 3 5 7 9'
            return
            ;;
        -o* | -w?*)
            compopt -o filenames
            _comp_compgen -P "${cur:0:2}" -- -d -S/
            compopt -o nospace
            return
            ;;
        -r?*)
            _comp_compgen -P "-r" -- -W '- 0'
            return
            ;;
        -scs*)
            _comp_compgen -P "-scs" -- -W 'UTF-8 WIN DOS'
            return
            ;;
        -ssc?*)
            _comp_compgen -P "-ssc" -- -W '-'
            return
            ;;
        -t*)
            if [[ $mode == w ]]; then
                _comp_compgen -P "-t" -- -W '7z bzip2 gzip swfc tar wim xz zip'
            else
                _comp_compgen -P "-t" -- -W '7z apm arj bzip2 cab chm cpio
                    cramfs deb dmg elf fat flv gzip hfs iso lzh lzma lzma86
                    macho mbr mslz mub nsis ntfs pe ppmd rar rpm squashfs swf
                    swfc tar udf vhd wim xar xz z zip'
            fi
            return
            ;;
        -m*=* | -p* | -u* | -v*)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen -- -W '-ai -an -ao -ax -bd -i -m{x,s,f,he,hc,mt}=
            -o -p -r -scs -sfx -si -slp -slt -so -ssc -t -u -v -w -x -y'
        [[ ${COMPREPLY-} == -@(an|bd|sfx|si|slt|so|ssc|[rwy]) ]] ||
            compopt -o nospace
        return
    fi

    local REPLY
    _comp_count_args
    if ((REPLY == 2)); then
        _comp_compgen_filedir_xspec unzip
        # TODO: parsing 7z i output?
        # - how to figure out if the format is input or output?
        # - find string Formats:, read until next empty line
        # - extensions start from column 26
        #   - ignore everything in parens
        #   - terminate on two spaces
        #   - terminate on token containing anything [^a-z0-9]
        #     (assumption: extensions are all lowercase)
        [[ $mode == w ]] &&
            _comp_compgen -a filedir '@(7z|bz2|swf|?(g)tar|?(t)[bglx]z|tb?(z)2|wim)' ||
            _comp_compgen -a filedir '@(7z?(.001)|arj|bz2|cab|cb7|chm|cpio|deb|dmg|flv|gem|img|iso|lz[ah]|lzma?(86)|msi|pmd|[rx]ar|rpm|sw[fm]|?(g)tar|taz|?(t)[bglx]z|tb?(z)2|vhd|wim|Z)'
    else
        if [[ ${words[1]} == d ]]; then
            _comp_compgen_split -l -- "$(
                "$1" l "${words[2]}" -slt 2>/dev/null | command sed -n \
                    's/^Path = \(.*\)$/\1/p' 2>/dev/null | _comp_tail -n +2
            )"
            compopt -o filenames
        else
            _comp_compgen_filedir
        fi
    fi
} &&
    complete -F _comp_cmd_7z 7z 7za 7zr 7zz 7zzs

# ex: filetype=sh
