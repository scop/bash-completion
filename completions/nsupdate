# bash completion for nsupdate(1)                          -*- shell-script -*-

_comp_cmd_nsupdate()
{
    local cur prev words cword comp_args
    _comp_initialize -- "$@" || return

    case $prev in
        -*[VLprtu])
            return
            ;;
        -*k)
            _comp_compgen_filedir key
            return
            ;;
        -*R)
            _comp_compgen -c "${cur:-/dev/}" filedir
            return
            ;;
        -*y)
            if [[ $cur == h* ]]; then
                _comp_comtpen -- -W "hmac-{md5,sha{1,224,256,384,512}}" -S :
                [[ ${COMPREPLY-} == *: ]] && compopt -o nospace
            fi
            return
            ;;
    esac

    if [[ $cur == -* ]]; then
        _comp_compgen_usage
        return
    fi

    _comp_compgen_filedir
} &&
    complete -F _comp_cmd_nsupdate nsupdate

# ex: filetype=sh
