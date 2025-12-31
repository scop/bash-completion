# freeciv client completions                               -*- shell-script -*-

_comp_cmd_freeciv()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        --help | --version | --name | --port | -[hvnp])
            return
            ;;
        --file | --log | --music | --read | --Sound | --tiles | -[flmrSt])
            _comp_compgen_filedir
            return
            ;;
        --Announce | -A)
            _comp_compgen -- -W 'IPv4 IPv6 none'
            return
            ;;
        --debug | -d)
            _comp_compgen -- -W '{0..3}'
            return
            ;;
        --Meta | --server | -[Ms])
            _comp_compgen_known_hosts -- "$cur"
            return
            ;;
        --Plugin | -P)
            _comp_compgen -- -W 'none esd sdl'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help
    fi

} &&
    complete -F _comp_cmd_freeciv freeciv{,-{gtk{2,3},sdl,xaw}} civclient

# ex: filetype=sh
