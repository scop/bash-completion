# pine/alpine completion                                   -*- shell-script -*-

_comp_cmd_pine()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -help | -d | -f | -c | -I | -n | -url | -copy_pinerc | -copy_abook)
            return
            ;;
        -attach | -attachlist | -attach_and_delete | -p | -P | -pinerc | \
            -passfile | -x)
            _comp_compgen_filedir
            return
            ;;
        -sort)
            _comp_compgen -- -W 'arrival subject threaded orderedsubject date
                from size score to cc'
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_help -- -h
    else
        _comp_compgen_split -- "$(_comp_awk '{print $1}' ~/.addressbook 2>/dev/null)"
    fi
} &&
    complete -F _comp_cmd_pine pine alpine

# ex: filetype=sh
