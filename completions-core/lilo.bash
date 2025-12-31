# bash completion for lilo(8)                              -*- shell-script -*-

_comp_cmd_lilo__labels()
{
    _comp_compgen_split -- "$(_comp_awk -F = '$1 ~ /^[ \t]*label$/ {print $2}' \
        "${1:-/etc/lilo.conf}" 2>/dev/null | command sed -e 's/\"//g')"
}

_comp_cmd_lilo()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -C | -i | -m | -s | -S)
            _comp_compgen_filedir
            return
            ;;
        -r)
            _comp_compgen_filedir -d
            return
            ;;
        -I | -D | -R)
            # label completion
            local i conf=""
            for i in "${!words[@]}"; do
                if [[ ${words[i]} == -C ]]; then
                    conf=${words[i + 1]-}
                    break
                fi
            done
            _comp_cmd_lilo__labels "$conf"
            return
            ;;
        -A | -b | -M | -u | -U)
            # device completion
            _comp_compgen -c "${cur:-/dev/}" filedir
            return
            ;;
        -T)
            # topic completion
            _comp_compgen -- -W 'help ChRul EBDA geom geom= table= video'
            return
            ;;
        -B)
            _comp_compgen_filedir bmp
            return
            ;;
        -E)
            _comp_compgen_filedir '@(bmp|dat)'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        # relevant options completion
        _comp_compgen -- -W '-A -B -b -c -C -d -E -f -g -i -I -l -L -m -M -p -P
            -q -r -R -s -S -t -T -u -U -v -V -w -x -z'
    fi
} &&
    complete -F _comp_cmd_lilo lilo

# ex: filetype=sh
