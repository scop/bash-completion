# json_xs completion                                       -*- shell-script -*-

_comp_cmd_json_xs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*f)
            _comp_compgen -- -W 'json cbor storable storable-file bencode clzf
                eval yaml string none'
            return
            ;;
        -*t)
            _comp_compgen -- -W 'json json-utf-8 json-pretty json-utf-16le
                json-utf-16be json-utf-32le json-utf-32be cbor storable
                storable-file bencode clzf yaml dump dumper string none'
            return
            ;;
        -*e)
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        _comp_compgen -a -- -W '-f'
    fi
} &&
    complete -F _comp_cmd_json_xs json_xs

# ex: filetype=sh
