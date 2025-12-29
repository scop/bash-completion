# lsof(8) completion                                       -*- shell-script -*-

_comp_cmd_lsof()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -'?' | -h | +c | -c | -d | -F | -i | +r | -r | -s | -S | -T)
            return
            ;;
        -A | -k | -m | +m | -o)
            _comp_compgen_filedir
            return
            ;;
        +d | +D)
            _comp_compgen_filedir -d
            return
            ;;
        -D)
            _comp_compgen -- -W '? b i r u'
            return
            ;;
        -f)
            _comp_compgen -- -W 'c f g G n'
            return
            ;;
        -g)
            # TODO: handle ^foo exclusions, comma separated lists
            _comp_compgen_pgids
            return
            ;;
        -p)
            # TODO: handle ^foo exclusions, comma separated lists
            _comp_compgen_pids
            return
            ;;
        -u)
            # TODO: handle ^foo exclusions, comma separated lists
            _comp_compgen -- -u
            return
            ;;
    esac

    if [[ $cur == [-+]* ]]; then
        _comp_compgen -- -W '-h -a -A -b -c +c -C +d -d +D -D +f -f -F -g -i -k
            -l +L -L +m -m +M -M -n -N -o -O -p -P +r -r -R -s -S -T -t -u -U
            -v -V +w -w -x -X -z -Z'
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_lsof lsof

# ex: filetype=sh
