# optipng(1) completion                                    -*- shell-script -*-

_comp_cmd_optipng()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -'?' | -h | --help | -f)
            return
            ;;
        -o)
            _comp_compgen -- -W '{0..7}'
            return
            ;;
        -out | -log)
            _comp_compgen_filedir
            return
            ;;
        -dir)
            _comp_compgen_filedir -d
            return
            ;;
        -i)
            _comp_compgen -- -W '0 1'
            return
            ;;
        -zc | -zm)
            _comp_compgen -- -W '{1..9}'
            return
            ;;
        -zw)
            _comp_compgen -- -W '256 512 1k 2k 4k 8k 16k 32k'
            return
            ;;
        -strip)
            _comp_compgen -- -W 'all'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
        return
    fi

    _comp_compgen_filedir '@(png|bmp|gif|pnm|tif?(f))'
} &&
    complete -F _comp_cmd_optipng optipng

# ex: filetype=sh
