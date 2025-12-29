# bash completion for mkisofs/genisoimage                  -*- shell-script -*-

_comp_cmd_mkisofs()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -o | -abstract | -biblio | -check-session | -copyright | -log-file | \
            -root-info | -prep-boot | -*-list)
            _comp_compgen_filedir
            return
            ;;
        -*-charset)
            _comp_compgen_split -- "$(mkisofs -input-charset help 2>&1 |
                tail -n +3)"
            return
            ;;
        -uid)
            _comp_compgen_uids
            return
            ;;
        -gid)
            _comp_compgen_gids
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -help
    else
        _comp_compgen_filedir
    fi

} &&
    complete -F _comp_cmd_mkisofs mkisofs genisoimage

# ex: filetype=sh
