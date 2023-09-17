# geoiplookup(1) completion                                -*- shell-script -*-

_comp_cmd_geoiplookup()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -h | -'?' | -v)
            return
            ;;
        -d)
            _comp_compgen_filedir -d
            return
            ;;
        -f)
            _comp_compgen_filedir dat
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage -- -h
        return
    fi

    local ipvx
    [[ $1 == *6 ]] && ipvx=-6 || ipvx=-4
    _comp_compgen_known_hosts $ipvx -- "$cur"
} &&
    complete -F _comp_cmd_geoiplookup geoiplookup geoiplookup6

# ex: filetype=sh
