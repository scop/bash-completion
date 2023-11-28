# fusermount completion                                    -*- shell-script -*-

_comp_cmd_fusermount()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[hVo])
            return
            ;;
        -*u)
            _comp_compgen_split -- "$(_comp_awk \
                '{ if ($3 ~ /^fuse(\.|$)/) print $2 }' /etc/mtab 2>/dev/null)"
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
    else
        _comp_compgen_filedir -d
    fi
} &&
    complete -F _comp_cmd_fusermount fusermount

# ex: filetype=sh
